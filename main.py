import asyncio

from loguru import logger
from pyrogram import Client

chat_id = -10012332534
my_emoji = "👍"

api_id = 12345678
api_hash = "345dsffsad98934dsgf884g"

client = Client("my_account", api_id=api_id, api_hash=api_hash)


async def main():
    async with client:
        async for message in client.get_chat_history(chat_id):
            try:
                username = message.from_user.username
                message_text = message.text
                message_id = message.id
                if message.reactions:
                    emoji = message.reactions[0].emoji
                else:
                    emoji = None
                if emoji != my_emoji:
                    await client.send_reaction(message_id=message_id, chat_id=chat_id, emoji=my_emoji)
                    logger.success(f"\n"
                                   f"Username: @{username}\n"
                                   f"Message_ID: {message_id}\n"
                                   f"Message_Text: {message_text}\n\n")
            except:
                logger.error(f"\n"
                             f"Username: @{username}\n"
                             f"Message_ID: {message_id}\n"
                             f"Message_Text: {message_text}\n\n")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
