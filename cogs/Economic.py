"""
This file holds all the commands for the Economic/Currency system.
Copyright (c) 2022 Mathavan Pirathaban
"""

from discord.ext import commands
import json
import discord
import random
import operator
from constant import BOT_ID

class Economic(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


#---------------------Helper Functions------------------
  async def get_users(self):
    """
    This function open the bank json file, loads it and returns it.
    """
    with open("jsons/bank.json", "r") as file:
      users = json.load(file)
    return users


  async def get_jobs(self):
    """
    This function open the jobs json file, loads it and returns it.
    """
    with open("jsons/jobs.json", "r") as file:
      jobs = json.load(file)
    return jobs


  async def get_items(self):
    """
    This function open the items json file, loads it and returns it.
    """
    with open("jsons/items.json", "r") as file:
      items = json.load(file)
    return items


  async def update_users(self, users_json):
    """
    This function updates the bank.json file.
    """
    with open("jsons/bank.json", "w") as file:
      json.dump(users_json, file)
    return


  async def open_bank_account(self, user):
    """
    This helper function open a bank account for the user.
    """
    users = await self.get_users()
    if str(user.id) in users:
      return
    else:
      users[str(user.id)] = {}
      users[str(user.id)]["Wallet"] = 0
      users[str(user.id)]["Bank"] = 0
      users[str(user.id)]["Inventory"] = {}
      users[str(user.id)]["Job"] = {}
    await self.update_users(users)
    return


  async def send_jobs_embed(self, ctx):
    """
    This function send the list of jobs as an embed.
    """
    jobs = await self.get_jobs()
    embed = discord.Embed(
      title = "List of Jobs and their Earning 🤑",
      color = discord.Color.from_rgb(252, 144, 3)
    )
    for key, val in jobs.items():
      name_field = val["Position"] + " " + val["Emoji"] + "  =  " + str(val["Salary"]) + " 🪙"
      embed.add_field(
        name = name_field,
        value = '\u200b',
        inline = False
      )
    await ctx.channel.send(embed=embed)
    return


#-------------------The Commands---------------------------
  @commands.command(aliases = ["bal"])
  async def balance(self, ctx):
    """
    This commands will let the users to check their balance in their wallet and in their bank account.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    wallet_amount = str(users[str(ctx.author.id)]["Wallet"])
    bank_amount = str(users[str(ctx.author.id)]["Bank"])
    embed = discord.Embed(
      title = f"{ctx.author.name}'s wealth information.",
      color = discord.Color.from_rgb(40, 173, 51)
    )
    embed.set_thumbnail(url = ctx.author.display_avatar.url)
    embed.add_field(
      name = f"👛 Wallet balance",
      value = wallet_amount,
      inline = False
    )
    embed.add_field(
      name = f"🏦 Bank balance",
      value = bank_amount,
      inline = False
    )
    await ctx.channel.send(embed=embed)
    return


  @commands.command(pass_context=True)
  @commands.cooldown(1, 60*60*3, commands.BucketType.user)
  async def beg(self, ctx):
    """
    This command donates the user some coins every three hours when the user begs for it.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    amount = random.randrange(5,50)
    users[str(ctx.author.id)]["Wallet"] += amount
    await self.update_users(users)
    await ctx.channel.send(f"Oh poor {ctx.author.mention}! Here take {amount} 🪙")
    return


  @commands.command(pass_context=True)
  @commands.cooldown(1, 60*60*24, commands.BucketType.user)
  async def daily(self, ctx):
    """
    This command rewards the user some coins for daily login.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    amount = 100
    users[str(ctx.author.id)]["Wallet"] += amount
    await self.update_users(users)
    await ctx.channel.send(f"Hello {ctx.author.mention}! Here is your daily reward {amount} 🪙")
    return


  @commands.command(aliases = ["dep"])
  async def deposit(self, ctx, *, amount="0"):
    """
    This command lets the user deposit amount of money from their wallet to their bank account.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    if amount.lower() == "all":
      amount = int(users[str(ctx.author.id)]["Wallet"])
    elif int(amount) < 0:
      await ctx.channel.send(f"{ctx.author.mention} enter a valid amount 😤")
      return
    elif int(amount) == 0:
      await ctx.channel.send(f"Come on {ctx.author.mention}! You need to enter an amount")
      return
    if (int(amount) > int(users[str(ctx.author.id)]["Wallet"])):
      await ctx.channel.send(f"Yo {ctx.author.mention}! You do not have that much coins in your wallet 🤣")
      return
    users[str(ctx.author.id)]["Wallet"] -= int(amount)
    users[str(ctx.author.id)]["Bank"] += int(amount)
    await self.update_users(users)
    await self.balance(ctx)
    return


  @commands.command(pass_context = True)
  @commands.cooldown(1, 60*5, commands.BucketType.user)
  async def steal(self, ctx, *, member: discord.Member):
    """
    This command lets the user to steal some portion of coins from the member's wallet. If got caught, the user pays some hefty fees to the BOT.
    """
    await self.open_bank_account(ctx.author)
    await self.open_bank_account(member)
    users = await self.get_users()
    if (int(users[str(member.id)]["Wallet"]) <= 5):
      await ctx.channel.send(f"{ctx.author.mention}! {member.name} is too broke that you cannot steal any coins 😥")
      ctx.command.reset_cooldown(ctx)
      return
    max_steal = int(users[str(member.id)]["Wallet"] * 0.75)
    max_steal = random.randrange(2, max_steal)
    steal_chance = random.randrange(0, 3)
    if (steal_chance == 1) or (steal_chance == 2):
      users[str(member.id)]["Wallet"] -= max_steal
      users[str(ctx.author.id)]["Wallet"] += max_steal
      await self.update_users(users)
      await ctx.channel.send(f"{ctx.author.mention} stole {max_steal} 🪙 from {member.name}")
      return
    wallet_lose = int(users[str(ctx.author.id)]["Wallet"] * 0.1)
    bank_lose = int(users[str(ctx.author.id)]["Bank"] * 0.05)
    users[str(ctx.author.id)]["Wallet"] -= wallet_lose
    users[str(ctx.author.id)]["Bank"] -= bank_lose
    users[BOT_ID]["Bank"] += wallet_lose
    users[BOT_ID]["Bank"] += bank_lose
    await self.update_users(users)
    await ctx.channel.send(f"Uh Oh {ctx.author.mention}!, you got caught by the police while stealing {member.name}. As a result, you are fined {wallet_lose} 🪙 from your Wallet and {bank_lose} 🪙 from your Bank 🤕")
    return


  @commands.command()
  async def send(self, ctx, amount = 0, *, member: discord.Member):
    """
    This command lets the user send some money from their bank account to the member's wallet.
    """
    await self.open_bank_account(ctx.author)
    await self.open_bank_account(member)
    users = await self.get_users()
    if amount <= 0:
      await ctx.channel.send(f"{ctx.author.mention}! you need to enter a valid amount when sending a user 🪙. For e.g  $send 50 @user")
      return
    if amount > users[str(ctx.author.id)]["Bank"]:
      await ctx.channel.send(f"{ctx.author.mention} who are you kidding? You do not have that much money in your bank account 🤭")
      return
    users[str(ctx.author.id)]["Bank"] -= amount
    users[str(member.id)]["Wallet"] += amount
    await self.update_users(users)
    await ctx.channel.send(f"{ctx.author.mention}! The transaction was successful! You have send {amount} 🪙 to {member.name}")
    return


  @commands.command(pass_context = True)
  @commands.cooldown(1, 60*30, commands.BucketType.user)
  async def rob(self, ctx):
    """
    This command lets the user rob the bank and get some portion of money. If get caught, they pay the bank a hef
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    if (int(users[str(BOT_ID)]["Bank"]) < 10000):
      await ctx.channel.send(f"{ctx.author.mention}! The Bank does not have enough money to rob. 😢")
      ctx.command.reset_cooldown(ctx)
      return
    max_steal = random.randrange(1000, 10000)
    steal_chance = random.randrange(0, 20)
    if (steal_chance == 5):
      users[str(BOT_ID)]["Bank"] -= max_steal
      users[str(ctx.author.id)]["Wallet"] += max_steal
      await self.update_users(users)
      await ctx.channel.send(f"{ctx.author.mention} stole {max_steal} 🪙 from the Bank")
      return
    wallet_lose = int(users[str(ctx.author.id)]["Wallet"] * 0.15)
    bank_lose = int(users[str(ctx.author.id)]["Bank"] * 0.1)
    users[str(ctx.author.id)]["Wallet"] -= wallet_lose
    users[str(ctx.author.id)]["Bank"] -= bank_lose
    users[BOT_ID]["Bank"] += wallet_lose
    users[BOT_ID]["Bank"] += bank_lose
    await self.update_users(users)
    await ctx.channel.send(f"Uh Oh {ctx.author.mention}!, you got caught by the police while stealing the bank. As a result, you are fined {wallet_lose} 🪙 from your Wallet and {bank_lose} 🪙 from your Bank 🤕")
    return


  @commands.command(pass_context = True)
  @commands.cooldown(1, 60*5, commands.BucketType.user)
  async def job(self, ctx, *, position = "None"):
    """
    This command lets the user apply for a job every 5 minutes.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    jobs = await self.get_jobs()
    for key, val in jobs.items():
      if (position.lower() == key):
        position = val["Position"]
        accept = random.randrange(0, int(val["Chance"]))
        if accept == 1:
          users[str(ctx.author.id)]["Job"]["Position"] = position
          users[str(ctx.author.id)]["Job"]["Salary"] = val["Salary"]
          users[str(ctx.author.id)]["Job"]["Chance"] = val["Chance"]
          await self.update_users(users)
          await ctx.channel.send(f"{ctx.author.mention} congratulations on your new job as the {position} 🥳")
          return
        else:
          await ctx.channel.send(f"{ctx.author.mention} your job application is rejected for being {position} 😪")
          return
    await ctx.channel.send(f"{ctx.author.mention} you need to enter a valid job title. For e.g $job waiter 😒")
    await self.send_jobs_embed(ctx)
    ctx.command.reset_cooldown(ctx)
    return


  @commands.command(aliases = ["joblis", "jobl", "joblist", "joblists", "listjob"])
  async def listjobs(self, ctx):
    """
    This command list all the jobs and their salary
    """
    await self.send_jobs_embed(ctx)
    return


  @commands.command(pass_context = True)
  @commands.cooldown(1, 60*60*12, commands.BucketType.user)
  async def work(self, ctx):
    """
    This command lets the user work for every 12. Successfull completition of work means, full salary. Otherwise half for the effort.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    if users[str(ctx.author.id)]["Job"] == {}:
      await ctx.channel.send(f"{ctx.author.mention} you don't have a job to work. Find a job using $job 😑")
      await self.send_jobs_embed(ctx)
      ctx.command.reset_cooldown(ctx)
      return
    guess_num = random.randrange(1, 6)
    await ctx.channel.send(f"{ctx.author.mention} guess a number between 1 and 5")
    def check(msg):
      if (str(msg.content) in "1 2 3 4 5") and msg.channel == ctx.channel and msg.author == ctx.author:
        return True
      return False
    user_input = await self.bot.wait_for("message", timeout = 20, check=check)
    earn = int(users[str(ctx.author.id)]["Job"]["Salary"] * 0.5)
    completition = f"did not guess the number right. I was thinking {guess_num}, but do not worry here is some for your effort"
    if int(user_input.content) == guess_num:
      earn = users[str(ctx.author.id)]["Job"]["Salary"]
      completition = "correctly guessed the number I was thinking, here is your salary"
    users[str(ctx.author.id)]["Wallet"] += earn
    await self.update_users(users)
    await ctx.channel.send(f"{ctx.author.mention} you have {completition} {earn} 🪙 ")
    return


  @commands.command(aliases = ['inv'])
  async def inventory(self, ctx):
    """
    This function send an embed of the items in the user's inventory.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    items = await self.get_items()
    embed = discord.Embed(
      title = f"{ctx.author.name}'s inventory",
      color = discord.Color.from_rgb(242, 145, 255)
    )
    embed.set_thumbnail(url = ctx.author.display_avatar.url)
    for key, val in users[str(ctx.author.id)]["Inventory"].items():
      if val != 0:
        item_name = items[key]["Name"] + " " + items[key]["Emoji"] + "  x " + str(val)
        embed.add_field(
          name = item_name,
          value = '\u200b',
          inline = False
        )
    await ctx.channel.send(embed=embed)
    return


  @commands.command(pass_context = True)
  @commands.cooldown(1, 60*60, commands.BucketType.user)
  async def dig(self, ctx):
    """
    This command lets the user dig the ground every 1hr and obtain an item.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    item = await self.get_items()
    found = random.randrange(0, 100)
    if found > 50:
      await ctx.channel.send(f"Unlucky {ctx.author.mention}, you have found nothing 😭")
      return
    the_item = "Bone"
    the_item_emoji = "🦴"
    for key, val in item.items():
      if found in val["Chance"]:
        if key in users[str(ctx.author.id)]["Inventory"]:
          users[str(ctx.author.id)]["Inventory"][key] += 1
        else:
          users[str(ctx.author.id)]["Inventory"][key] = 1
        the_item = val["Name"]
        the_item_emoji = val["Emoji"]
    #Bone found
    if "bone" in users[str(ctx.author.id)]["Inventory"]:
      users[str(ctx.author.id)]["Inventory"][key] += 1
    else:
      users[str(ctx.author.id)]["Inventory"][key] = 1
    await self.update_users(users)
    await ctx.channel.send(f"Woah {ctx.author.mention}, you have found {the_item}{the_item_emoji}")
    return


  @commands.command()
  async def sell(self, ctx, item = "None", num = 1):
    """
    This command lets the user to sell the num of item from their inventory.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    item_json = await self.get_items()
    if item == "None":
      await ctx.channel.send(f"{ctx.author.mention}, you need to enter an item that you want to sell 🙄")
      return
    elif str(item).lower() == "all":
      #Sell all items
      profit = 0
      for key, val in users[str(ctx.author.id)]["Inventory"].items():
        if val != 0:
          for i in range(val):
            users[str(ctx.author.id)]["Wallet"] += item_json[key]["Price"]
            profit += item_json[key]["Price"]
            users[str(ctx.author.id)]["Inventory"][key] -= 1
            await self.update_users(users)
      await ctx.channel.send(f"{ctx.author.mention}, you have sold all your item(s) for {profit} 🪙")
      return
    else:
      for key, val in users[str(ctx.author.id)]["Inventory"].items():
        if str(item).replace(" ", "") in item_json[key]["Name"].lower():
          if val == 0:
            await ctx.channel.send(f"{ctx.author.mention}, you do not have enough of this item 🤣")
            return
          else:
            if int(num) <= val:
              amount = 0
              for j in range(int(num)):
                users[str(ctx.author.id)]["Wallet"] += item_json[key]["Price"]
                amount += item_json[key]["Price"]
                users[str(ctx.author.id)]["Inventory"][key] -= 1
                await self.update_users(users)
              sold_item = item_json[key]["Name"]
              sold_item_emoji = item_json[key]["Emoji"]
              sold_item_price = item_json[key]["Price"]
              await ctx.channel.send(f"{ctx.author.mention}, has sold {sold_item} {sold_item_emoji} for {sold_item_price}🪙")
              return
    await ctx.channel.send(f"{ctx.author.mention}, Invalid item or you do not have this item in your inventory 😤")
    return


  @commands.command(aliases = ["lb"])
  async def leaderboard(self, ctx):
    """
    This command sends an embed of the top 10 or less richest users in the server.
    """
    await self.open_bank_account(ctx.author)
    users = await self.get_users()
    leader_board = {}
    for key, val in users.items():
      user_id = int(key)
      total_money = val["Wallet"] + val["Bank"]
      leader_board[user_id] = total_money
    leader_board = sorted(leader_board.items(), key=operator.itemgetter(1), reverse=True)
    embed = discord.Embed(
      title = "Top richest users in the server",
      color = discord.Color.from_rgb(3, 252, 198)
    )
    ten = 0
    for i in range(len(leader_board)):
      if 10 > ten:
        user_id = leader_board[i][0]
        member = ctx.guild.get_member(int(user_id))
        if member != None:
          name_field = f"{i+1}. " + str(member.name) + "  =  " + str(leader_board[i][1]) + " 🪙"
          embed.add_field(
            name = name_field,
            value = '\u200b',
            inline = False
          )
          ten += 1
    await ctx.channel.send(embed=embed)
    return


async def setup(bot):
  await bot.add_cog(Economic(bot))
