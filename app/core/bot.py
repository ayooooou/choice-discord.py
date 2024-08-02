import discord
from discord.ext import commands
import core.main as main

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

main.register(bot)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")