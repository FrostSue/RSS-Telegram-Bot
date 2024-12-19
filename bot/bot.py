import asyncio
import logging

from typing import List, Dict
from configparser import ConfigParser

from pyrogram import Client, filters, idle
from pyrogram.enums import ParseMode
from pyrogram.errors import RPCError

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .database import DatabaseManager
from .rss_handler import RSSHandler


class RSSBot:
    def __init__(self, config_path="config.ini"):
        self.config = ConfigParser()
        self.config.read(config_path)

        self.database = DatabaseManager()
        self.rss_handler = RSSHandler(
            self.config["RSS"]["FEED_URL"]
        )

        self.client = Client(
            "rss_bot",
            api_id=self.config["Telegram"]["API_ID"],
            api_hash=self.config["Telegram"]["API_HASH"],
            bot_token=self.config["Telegram"]["BOT_TOKEN"]
        )

        self.scheduler = AsyncIOScheduler()

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self._register_handlers()

    def _register_handlers(self):
        @self.client.on_message(filters.command("start"))
        async def start_command(client, message):
            await message.reply_text("📡 RSS Bot aktif!")

        @self.client.on_message(filters.command("recent"))
        async def recent_entries(client, message):
            recent = self.database.get_recent_entries(5)
            if recent:
                response = "**Son 5 içerik:**\n\n"
                for _, title, link in recent:
                    response += f"**• [{title}]({link})**\n\n"
                await message.reply_text(response)
            else:
                await message.reply_text("Henüz içerik yok.")

    async def _check_rss_and_send(self):
        try:
            new_entries = self.rss_handler.fetch_new_entries(self.database)
            for entry in new_entries:
                message = (
                    f"📰 **Yeni İçerik**\n\n"
                    f"**{entry["title"]}**\n\n"
                    f"[Devamını Oku]({entry["link"]})"
                )
                
                try:
                    await self.client.send_message(
                        chat_id=self.config["Telegram"]["CHAT_ID"],
                        text=message,
                        parse_mode=ParseMode.MARKDOWN
                    )
                except RPCError as e:
                    self.logger.error(f"Mesaj gönderme hatası: {e}")

        except Exception as e:
            self.logger.error(f"RSS kontrol hatası: {e}")

    async def start(self):
        interval = int(self.config["RSS"]["CHECK_INTERVAL"])
        self.scheduler.add_job(
            self._check_rss_and_send, 
            "interval", 
            hours=interval,
            max_instances=2
        )
        
        self.scheduler.start()

        await self.client.start()

        await idle()

    async def stop(self):
        self.scheduler.shutdown()
        await self.client.stop()
