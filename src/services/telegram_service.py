import httpx

from lib.config import settings
from lib.loggers import root_logger


class TelegramService:
    def __init__(self):
        self.token = settings.TELEGRAM_TOKEN
        self.base_url = f"https://api.telegram.org/bot{self.token}"
        self.client = httpx.AsyncClient()

    async def send_message(self, chat_id: str, text: str):
        url = f"{self.base_url}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        try:
            response = await self.client.post(url, json=payload)
            response.raise_for_status()
            root_logger.info(f"Message sent to {chat_id}")
        except httpx.HTTPStatusError as e:
            root_logger.error(f"Failed to send message to {chat_id}: {e.response.text}")
        except Exception as e:
            root_logger.error(f"Error sending message to {chat_id}: {e}")

    async def close(self):
        await self.client.aclose()
