import json
import asyncio
from datetime import datetime

from lib.loggers import root_logger
from src.models.v1.models import Alert
from src.producers.v1.alert_producer import AlertProducer
from connections.db_connection import get_db_connection

class DBAlertPoller:
    def __init__(self, poll_interval: int = 60):
        self.poll_interval = poll_interval
        self.producer = AlertProducer()
        self.running = False

    async def start(self):
        await self.producer.start()
        self.running = True
        root_logger.info("DB Alert Poller started")
        asyncio.create_task(self.poll())

    async def poll(self):
        while self.running:
            try:
                root_logger.info(f"Alerts read try: {datetime.now()}")
                conn = await get_db_connection()
                try:
                    rows = await conn.fetch("SELECT * FROM alerts.alerts WHERE status = 'new'")
                    for row in rows:
                        alert = Alert(
                            layer=row['layer'],
                            service=row['service'],
                            function=row['function'],
                            error=row['error'],
                            comment=row['comment'],
                            datetime=row['datetime'].isoformat()
                        )
                        
                        await self.producer.send_alert(alert)
                        
                        await conn.execute(
                            "UPDATE alerts.alerts SET status = 'sent' WHERE id = $1",
                            row['id']
                        )
                        root_logger.info(f"Processed alert ID {row['id']} from DB")
                finally:
                    await conn.close()
            except Exception as e:
                root_logger.error(f"Error in DB polling loop: {e}")
            
            await asyncio.sleep(self.poll_interval)

    async def stop(self):
        self.running = False
        await self.producer.stop()
        root_logger.info("DB Alert Poller stopped")
