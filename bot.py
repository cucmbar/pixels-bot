import os
from dotenv import load_dotenv
import asyncio
import telegram

load_dotenv()

async def main():
    bot = telegram.Bot(os.getenv('TOKEN'))
    async with bot:
        print(await bot.get_me())

print(os.getenv('TOKEN'))

#if __name__ ==  '__main__':
    #asyncio.run(main())