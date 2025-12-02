import asyncio
from src.consumers.v1.alerts_consumer import AlertsConsumer
from src.producers.v1.db_alert_poller import DBAlertPoller
from lib.loggers import root_logger

async def main():
    consumer = AlertsConsumer()
    poller = DBAlertPoller()
    
    await consumer.start()
    await poller.start()
    
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    finally:
        await consumer.stop()
        await poller.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
