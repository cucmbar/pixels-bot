import os
from dotenv import load_dotenv
import asyncio
from telegram import Update
import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a monnster, please kill me!")

async def kill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='you killed me!')

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    kill_handler = CommandHandler('kill', kill)
    application.add_handler(kill_handler)
    
    application.run_polling()


