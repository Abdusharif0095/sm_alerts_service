import json
from aiokafka import AIOKafkaConsumer

from lib.config import settings


def get_kafka_consumer() -> AIOKafkaConsumer:
    return AIOKafkaConsumer(
        settings.ALARMS_TOPIC,
        bootstrap_servers=settings.KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='latest'
    )
