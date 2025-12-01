import asyncio
from connections.kafka_connection import get_kafka_consumer
from src.services.telegram_service import TelegramService
from src.models.v1.models import Alert
from lib.config import settings
from lib.loggers import root_logger


class AlertsConsumer:
    def __init__(self):
        self.consumer = get_kafka_consumer()
        self.telegram_service = TelegramService()
        self.running = False

    async def start(self):
        await self.consumer.start()
        self.running = True
        root_logger.info("Alerts consumer started")
        asyncio.create_task(self.consume())

    async def consume(self):
        try:
            async for msg in self.consumer:
                if not self.running:
                    break
                try:
                    alert_data = msg.value
                    alert = Alert(**alert_data)
                    await self.process_alert(alert)
                except Exception as e:
                    root_logger.error(f"Error processing message: {e}")
        except Exception as e:
            root_logger.error(f"Critical error in consumer loop: {e}")
        finally:
            await self.stop()

    async def process_alert(self, alert: Alert):
        message_text = (
            f"<b>Layer:</b> {alert.layer.value}\n"
            f"<b>Service:</b> {alert.service}\n"
            f"<b>Function:</b> {alert.function}\n"
            f"<b>Error:</b> {alert.error}\n"
            f"<b>Time:</b> {alert.datetime}"
        )
        if alert.comment:
            message_text += f"\n<b>Comment:</b> {alert.comment}"

        for chat_id in settings.TELEGRAM_CHAT_IDS:
            await self.telegram_service.send_message(chat_id, message_text)

    async def stop(self):
        self.running = False
        await self.consumer.stop()
        await self.telegram_service.close()
        root_logger.info("Alerts consumer stopped")
