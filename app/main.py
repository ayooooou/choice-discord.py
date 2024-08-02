import os
from dotenv import load_dotenv
from core.bot import bot

if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("TOKEN"))