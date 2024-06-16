import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

# @app_commands.describe(參數名稱 = 參數敘述)
# 參數: 資料型態，可以限制使用者輸入的內容
# 參數: Optional[資料型態]，參數變成可選，可以限制使用者輸入的內容
@bot.tree.command(name = "say", description = "大聲說出來")
@app_commands.describe(name = "輸入人名", text = "輸入要說的話")
async def say(interaction: discord.Interaction, name: str, text: Optional[str] = None):
    if text == None:
        text = "。。。"
    await interaction.response.send_message(f"{name} 說 「{text}」")

# @app_commands.choices(參數 = [Choice(name = 顯示名稱, value = 隨意)])
@bot.tree.command(name = "order", description = "點餐機")
@app_commands.describe(meal = "選擇餐點", size = "選擇份量")
@app_commands.choices(
    meal = [
        Choice(name = "漢堡", value = "hamburger"),
        Choice(name = "薯條", value = "fries"),
        Choice(name = "雞塊", value = "chicken_nuggets"),
    ],
    size = [
        Choice(name = "大", value = 0),
        Choice(name = "中", value = 1),
        Choice(name = "小", value = 2),
    ]
)
async def order(interaction: discord.Interaction, meal: Choice[str], size: Choice[int]):
    # 獲取使用指令的使用者名稱
    customer = interaction.user.name
    # 使用者選擇的選項資料，可以使用name或value取值
    meal = meal.value
    size = size.value
    await interaction.response.send_message(f"{customer} 點了 {size} 號 {meal} 餐")
#--------------------------------------

import json

#新增
@bot.tree.command(name="addchoice", description="新增志願表")
@app_commands.describe(from_name="要新增的志願表名稱",option="總共志願數量",num="一個可以選多少志願")
async def addchoice(interaction: discord.Interaction, from_name: str, option:int ,num:int ):
    founder = interaction.user.name
    temp = {}
    temp["founder"] = founder
    temp["num"] = num
    await interaction.channel.send(f"<@{interaction.user.id}> 建立了 `{from_name}` 志願表，總共需輸入 `{option}` 個選項 ")
    values = []
    for i in range(option):
        await interaction.channel.send(f"請輸入第 {i+1} 個可選的志願名稱：")
        response = await bot.wait_for("message",timeout=6000.0, check=lambda m: m.author == interaction.user)
        values.append(response.content)
    temp["values"] = values
    with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'r') as f:
        data = json.load(f)
    data[from_name] = temp
    with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'w') as f:
        json.dump(data, f)
    response = await interaction.channel.send("設定完成，請打 /publishchoice 發布")


#發布
@bot.tree.command(name="publishchoice", description="新增志願表")
@app_commands.describe(from_name="要發布的志願表名稱")
async def publishchoice(interaction: discord.Interaction, from_name:str):
    with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'r') as f:
        data = json.load(f)
    choice = data[from_name]["values"]
    num = data[from_name]["num"]
    str1 = ""
    for i in choice:
        str1 += i
        str1 += ", "
    await interaction.response.send_message(f"`{from_name}`志願表已可填寫 志願分別有 `{str1}`，一人請選 `{num}` 個志願")


#選志願
from discord.ui import Select,View

@bot.tree.command(name="mychoice", description="新增志願表")
@app_commands.describe(from_name="要填寫的志願表名稱")
async def mychoice(interaction: discord.Interaction, from_name:str):
    with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'r') as f:
        data = json.load(f)
    nowoption=[]
    for i in data[from_name]["values"]:
        nowoption.append(discord.SelectOption(label=i , value=i))
        
    select=Select(options=nowoption,max_values=data[from_name]["num"])
    async def select_callback(interaction: discord.Interaction):
        await interaction.response.send_message(f"{select.values}")
    
    select.callback = select_callback
    view = View()
    view.add_item(select)
    await interaction.channel.send(view = view)
            
    # data[from_name][interaction.user.name]=your_values
    with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'w') as f:
        json.dump(data, f)
    await interaction.response.send_message(f"你正在填寫 `{from_name}`，請依順序填入你的志願")

#--------------------------------------

import os
from dotenv import load_dotenv
load_dotenv()
bot.run(os.getenv("TOKEN"))