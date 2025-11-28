import asyncio
from datetime import datetime

from src.models.v1.models import Alarm
from src.producers.v1.alarm_producer import AlarmProducer

async def main():
    producer = AlarmProducer()
    await producer.start()
    
    try:
        alarm = Alarm(
            service="Test Service",
            function="test_function",
            error="Test Error",
            datetime=datetime.now().isoformat(),
            comment="This is a test alarm"
        )
        
        await producer.send_alarm(alarm)
        print("Test alarm sent successfully")
        
    finally:
        await producer.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
