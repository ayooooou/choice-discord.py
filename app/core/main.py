import discord
import json

from typing import Optional
from discord import app_commands
from discord.ui import Select,View
from discord.app_commands import Choice


def register(bot):
    
    # 新增
    @bot.tree.command(name="addchoice", description="新增志願表")
    @app_commands.describe(from_name="要新增的志願表名稱", option="總共志願數量", num="一個可以選多少志願")
    async def addchoice(interaction: discord.Interaction, from_name: str, option: int, num: int):
        founder = interaction.user.name
        temp = {}
        temp["founder"] = founder
        temp["option"] = option
        temp["num"] = num
        temp["values"] = []

        with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'r') as f:
            data = json.load(f)
        data[from_name] = temp
        with open(r"C:\Users\yoyok\Documents\code\discordbot\choice\data.json", 'w') as f:
            json.dump(data, f)
        response = await interaction.channel.send("設定完成，請打 /publishchoice 發布")

    # 發布
    @bot.tree.command(name="publishchoice", description="發布志願表")
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
    @bot.tree.command(name="mychoice", description="填寫志願表")
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

    