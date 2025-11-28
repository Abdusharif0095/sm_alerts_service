import asyncio
from connections.kafka_connection import get_kafka_consumer
from src.services.telegram_service import TelegramService
from src.models.v1.models import Alarm
from lib.config import settings
from lib.loggers import root_logger

async def main():
    consumer = get_kafka_consumer()
    telegram_service = TelegramService()
    
    await consumer.start()
    root_logger.info("Kafka consumer started")
    
    try:
        async for msg in consumer:
            try:
                alarm_data = msg.value
                alarm = Alarm(**alarm_data)
                
                message_text = (
                    f"<b>Service:</b> {alarm.service}\n"
                    f"<b>Function:</b> {alarm.function}\n"
                    f"<b>Error:</b> {alarm.error}\n"
                    f"<b>Time:</b> {alarm.datetime}"
                )
                if alarm.comment:
                    message_text += f"\n<b>Comment:</b> {alarm.comment}"
                
                for chat_id in settings.TELEGRAM_CHAT_IDS:
                    await telegram_service.send_message(chat_id, message_text)
                    
            except Exception as e:
                root_logger.error(f"Error processing message: {e}")
                
    except Exception as e:
        root_logger.error(f"Critical error in main loop: {e}")
    finally:
        await consumer.stop()
        await telegram_service.close()
        root_logger.info("Service stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
