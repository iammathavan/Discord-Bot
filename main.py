"""
This is the main file and it runs  the code.
It have two functions that prints to the console if the bot is running and the
error handling on command error.

Copyright (c) 2022 Mathavan P
"""

from discord.ext import commands
import discord


from constant import BOT_TOKEN

intents = discord.Intents.all()
#The bot's prefix and the initialising the bot
bot = commands.Bot(command_prefix = ["$", "."], intents = intents, case_insensitive = True)


#Remove the default help command
bot.remove_command("help")


@bot.event
async def on_command_error(ctx, error):
  """
  This function will be triggered if the user who is using the command have an error. The respective error message will be send to the user through an embed.
  """
  #The user who have no permission
  if isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(
      title = "You are missing the permission",
      color = discord.Colour.red()
    )
    await ctx.channel.send(embed=embed)
  #The user using the command when they are in cooldown
  if isinstance(error, commands.CommandOnCooldown):
    seconds = int(error.retry_after)
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    await ctx.channel.send(f"Slow down {ctx.author.mention}! You can use this command again in {hours} hour(s) {minutes} minute(s) and {seconds} second(s)")
  """
  if isinstance(error, commands.CommandInvokeError):
    await ctx.channel.send(f"{ctx.author.mention} you took too long to respond.")
  """
  return


@bot.event
async def on_ready():
  """
  Executes when the bot is ready online.
  """
  print("The bot is ONLINE")
  #Set the bot's activity
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Football"))
  return

extensions = ['cogs.Fun', 'cogs.Admin', 'cogs.Economic', 'cogs.Help']

if __name__ == '__main__':
  for ext in extensions:
    await bot.load_extension(ext)



# Bot runs
bot.run(BOT_TOKEN)
