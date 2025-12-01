import asyncio
from datetime import datetime

from src.models.v1.models import Alert
from src.producers.v1.alert_producer import AlertProducer

async def main():
    producer = AlertProducer()
    await producer.start()
    
    try:
        alert = Alert(
            layer="python",
            service="Test Service",
            function="test_function",
            error="Test Error",
            datetime=datetime.now().isoformat(),
            comment="This is a test alert"
        )

        await producer.send_alert(alert)
        print("Test alert sent successfully")
        
    finally:
        await producer.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
