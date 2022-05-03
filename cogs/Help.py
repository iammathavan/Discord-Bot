"""
This file have all the commands that related to Help command.

Copyright (c) 2022 Mathavan Pirathaban
"""

from discord.ext import commands
import discord

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command = True)
  async def help(self, ctx):
    """
    This will trigger the bot to respond with all the commands.

    >>>$help
    {help embedded}
    """
    embed = discord.Embed(
      title = "Ronaldo Bot's Help Commands",
      description = "Use $help <command> to get more info about the command",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    embed.add_field(
      name = "Admin commands",
      value = "delete, kick, ban, unban",
      inline = True
    )
    embed.add_field(
      name = "Fun commands",
      value = "hello, mood, goal, inspire, stat, gif, meme, info, quote, pfp",
      inline = True
    )
    embed.add_field(
      name = "Economic commands",
      value = "balance, beg, daily, deposit, steal, send, rob, job, work, inventory, dig, sell, leaderboard",
      inline = True
    )
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def hello(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$hello",
      description = "Greets the you",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def mood(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$mood",
      description = "Express the bot's current mood",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def goal(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$goal",
      description = "Celebrates after scoring a goal",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def inspire(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$inspire",
      description = "Inspires you with a quote",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def stat(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$stat",
      description = "Display the statistics of the server",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def info(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$info",
      description = "Display the information about the user",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["giphy", "gifs"])
  async def gif(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$gif <keyword>",
      description = "Send a random gif related to the keyword.",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def meme(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$meme",
      description = "Send a random meme",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def quote(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$quote",
      description = "Send a random quote",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["profile-pic"])
  async def pfp(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$pfp <@user>",
      description = "Send profile picture of specified user",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["del"])
  async def delete(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$delete <num>",
      description = "Delete num of message(s) on the channel. Default delete limit set to 5.",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def kick(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$kick <@user>",
      description = "Kick the user from the server",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def ban(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$ban <@user>",
      description = "Ban the user from the server",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def unban(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$unban <@user>",
      description = "Unban the user from the server",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["bal"])
  async def balance(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$balance",
      description = "Checks your wallet and bank balance",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def beg(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$beg",
      description = "Begs the bot for some coins",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def daily(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$daily",
      description = "To claim daily reward",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["dep"])
  async def deposit(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$deposit <amount>",
      description = "Deposit amount of coins from your wallet to bank",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def steal(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$steal <@user>",
      description = "Steal some coins from the user",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def send(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$send <amount> <@user>",
      description = "Send amount of coins from your bank to the user's wallet",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def rob(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$rob",
      description = "Rob the bank",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def job(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$job <position>",
      description = "Apply for a job position",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def work(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$work",
      description = "Work in your job and earn coins",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["inv"])
  async def inventory(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$inventory",
      description = "List all the items in your inventory",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def dig(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$dig",
      description = "Dig in the ground and get an item",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command()
  async def sell(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$sell <item> <num>",
      description = "Sell the num of item in your inventory for coins",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return


  @help.command(aliases = ["lb"])
  async def leaderboard(self, ctx):
    """
    Extended command for help
    """
    embed = discord.Embed(
      title = "$leaderboard",
      description = "List the top richest 10 or less users in the server",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/cosmo-symbols/40/help_1-512.png")
    await ctx.channel.send(embed=embed)
    return



def setup(bot):
  bot.add_cog(Help(bot))
