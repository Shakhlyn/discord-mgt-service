import asyncio
import os

from discord_bot.bot_instance import bot

async def start_bot():
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        raise ValueError("Discord bot token is not found!")

    # To avoid blocking the FastAPI app by running bot in the background, we're creating task.
    asyncio.create_task(bot.start(token))