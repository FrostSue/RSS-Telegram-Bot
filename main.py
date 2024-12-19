import os
import asyncio

from bot.bot import RSSBot


async def main():
    if not os.path.exists("entries.db"):
        from bot.database import DatabaseManager
        DatabaseManager()

    bot = RSSBot()
    
    try:
        await bot.start()
    except KeyboardInterrupt:
        await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())
