import asyncio
from src.consumers.v1.alerts_consumer import AlertsConsumer
from lib.loggers import root_logger

async def main():
    consumer = AlertsConsumer()
    
    await consumer.start()
    
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass
    finally:
        await consumer.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
