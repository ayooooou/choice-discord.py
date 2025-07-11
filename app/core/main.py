import discord
import os
import json
from discord import app_commands
from discord.ui import Select,View

from core.__init__ import Choice
from core.sort import sort_choices

json_file_path = os.path.join(os.path.dirname(__file__), '../data/data.json')

def read_json():
    with open(json_file_path, 'r',encoding='utf-8') as f:
        data = json.load(f)
        return data

def write_json(data):
    with open(json_file_path, 'w',encoding='utf-8') as f:
        json.dump(data, f)
    

def register(bot):
    # 新增
    @bot.tree.command(name="add", description="新增志願表")
    @app_commands.describe(from_name="要新增的志願表名稱", option_num="總共志願數量")
    async def add(interaction: discord.Interaction, from_name: str, option_num: int):
        new = Choice(interaction.user.name,option_num)

        option_name = {}
        await interaction.response.defer(thinking=True)
        await interaction.channel.send(f"<@{interaction.user.id}> 建立了 `{from_name}`，要提供 `{option_num}` 個選項及需要人數")
        for i in range(option_num):
            # 等待用戶輸入值
            await interaction.channel.send(f"請輸入第 {i+1} 個選項及需要的人數 (例 總務:2)：")
            response = await bot.wait_for("message", check=lambda m: m.author == interaction.user,timeout=180.0)
            response=response.content.split(":")
            option_name[response[0]]=response[1]
        new.option_name = option_name
        
        data = read_json()
        data[from_name] = new.to_dict()
        write_json(data)
        response = await interaction.channel.send(f" `{from_name}` 設定完成， /publishchoice 發布")



    # 發布
    @bot.tree.command(name="publish", description="發布志願表")
    @app_commands.describe(from_name="要發布的志願表名稱")
    async def publish(interaction: discord.Interaction, from_name: str):
        data = read_json()
        if from_name not in data:
            await interaction.response.send_message(f"志願表 `{from_name}` 不存在", ephemeral=True)
            return  # 必加 return

        await interaction.response.defer()
        choice = data[from_name]["option_name"]
        str1 = "\n".join([f"- {k}: {v}人" for k, v in choice.items()])
        await interaction.followup.send(f"`{from_name}`志願表已發布 分別需要:\n{str1}\n\n`/fillout {from_name}` 進行填寫志願表")
    
    
    #選志願
    @bot.tree.command(name="fillout", description="填寫志願表")
    @app_commands.describe(from_name="要填寫的志願表名稱")
    async def fillout(interaction: discord.Interaction, from_name: str):
        data = read_json()
        
        if from_name not in data:
            await interaction.response.send_message(f"志願表`{from_name}` 不存在", ephemeral=True)
            return # 必加 return
        user_option_num = []
        for i in data[from_name]["option_name"]:
            user_option_num.append(discord.SelectOption(label=i, value=i))
    
        select = Select(options=user_option_num, max_values=data[from_name]["option_num"], placeholder="請選擇志願")

        async def select_callback(interaction: discord.Interaction):
            data[from_name]["people"][interaction.user.name] = select.values
            write_json(data)
            choices = "\n".join([f"第{i+1}志願 {choice}" for i, choice in enumerate(select.values)])
            await interaction.response.send_message(f"完成填寫 (請注意志願排序是否正確) \n\n{choices}")
    
        select.callback = select_callback
        view = View()
        view.add_item(select)
        await interaction.channel.send(f"填寫 `{from_name}`中...，請依順序填入你的志願 (注意:畫面上的排序不是您點的順序)", view=view)



    #排志願
    @bot.tree.command(name="sort", description="排序志願表")
    @app_commands.describe(from_name="要排序的志願表名稱")
    async def sort(interaction: discord.Interaction, from_name: str):
        data = read_json()
        
        if from_name not in data:
            await interaction.response.send_message(f"志願表名稱 `{from_name}` 不存在。請確認名稱是否正確。", ephemeral=True)
            
        result = sort_choices(data, from_name)
        data[from_name]["result"] = result
        
        write_json(data)
        result_str=""
        for str1 in result:
            result_str += f"\n- {str1} : {', '.join(result[str1])}"
        await interaction.response.send_message(f"`{from_name}` 排序完成 結果如下: {result_str}")