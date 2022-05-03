"""
This file holds all the fun user friendly commands.

Copyright (c) 2022 Mathavan Pirathaban
"""

from discord.ext import commands
import random
import discord
import giphy_client
from giphy_client.rest import ApiException
import requests
import json

from constant import (MOODS, GIPHY_API_KEY, REDDIT)

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  #----------------------Helper functions------------------

  def get_file_quotes(self):
    """
    Helper function that will read from the file and return a quote as the string randomly.
    """
    file = open("quotes.txt", "r")
    next_line = file.readline()
    list_of_quotes = []
    while next_line != "":
      if str(next_line) != "\n":
        list_of_quotes.append(str(next_line))
      next_line = file.readline()
    return random.choice(list_of_quotes)


  #----------------------Commands-----------------------------
  @commands.command()
  async def hello(self, ctx):
    """
    This will trigger the bot to greet the User.

    >>>$hello
    Hello there, {user}!
    """
    await ctx.channel.send(f"Hello there, {ctx.author.mention}!")
    return


  @commands.command()
  async def mood(self, ctx):
    """
    This will trigger the bot to express it's mood to the user.

    >>>$mood
    I am currently feeling {mood}!
    """
    mood = random.choice(MOODS)
    await ctx.channel.send(f"I am currently feeling {mood}!")
    return


  @commands.command()
  async def goal(self, ctx):
    """
    This will trigger the bot to respond to how it express after scoring a goal.

    >>>$goal
    I just scored a beautiful goal... Suiiiiiiiiiiiiiiiiiii!!!
    """
    await ctx.channel.send("I just scored a beautiful goal... Suiiiiiiiiiiiiiiiiiii!!!")
    return


  @commands.command()
  async def inspire(self, ctx):
    """
    This will trigger the bot to respond with a Cristiano Ronaldo quote back to the User.

    >>>$inspire
    >>>{Quote from Cristiano Ronaldo}
    """
    quote = self.get_file_quotes()
    await ctx.channel.send(quote)
    return


  @commands.command()
  async def stat(self, ctx):
    """
    This will trigger the bot to respond with the statistics of the server.

    >>>$stat
    {stats in embed}
    """
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    members = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(
      title=name + " Server Info:",
      description=description,
      color=discord.Colour.blurple()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Total Members", value=members, inline=True)
    await ctx.channel.send(embed=embed)
    return


  @commands.command(aliases = ["giphy", "gifs"])
  async def gif(self, ctx, *, q="Cristiano Ronaldo"):
    """
    This will trigger the bot to respond with a gif randomly from Giphy website. By default the bot will send gifs of Cristiano Ronaldo, however the user can type whatever keyword along with it to get some gifs related to the keyword.

    >>>$gif {keyword}
    {gif about the keyword}
    """
    api_instance = giphy_client.DefaultApi()
    try:
      api_response = api_instance.gifs_search_get(GIPHY_API_KEY, q, limit=30, rating="g")
      list_of_gifs = list(api_response.data)
      giff = random.choice(list_of_gifs)
      await ctx.channel.send(giff.embed_url)
    except ApiException as e:
      print("Exception when API called as " + str(e))
    return


  @commands.command()
  async def meme(self, ctx):
    """
    This will trigger the bot to respond to the user with a random trending meme from the subreddit meme.

    >>>$meme
    {meme from r/meme}
    """
    subreddit = REDDIT.subreddit("memes")
    hot_memes = list(subreddit.hot(limit=50))
    random_meme = random.choice(hot_memes)
    em = discord.Embed(title=random_meme.title)
    em.set_image(url=random_meme.url)
    await ctx.channel.send(embed=em)
    return


  @commands.command()
  async def info(self, ctx):
    """
    This will trigger the bot to respond to the user with the information about the user itself.

    >>>$info
    {info about the user}
    """
    user = ctx.author
    name = str(user.name)
    id = str(user.id)
    top_role = str(user.top_role)
    roles = str(len(user.roles))
    status = str(user.status)
    created = str(user.created_at.strftime("%d/%m/%Y %H:%M:%S"))
    if user.bot:
      is_bot = "Bot"
    else:
      is_bot = "Human"
    icon = str(user.avatar_url)
    embed = discord.Embed(
      title = user.display_name,
      description = "User Info",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name="Name", value=name, inline=True)
    embed.add_field(name="User ID", value=id, inline=True)
    embed.add_field(name="Human/Bot", value=is_bot, inline=True)
    embed.add_field(name="Top Role", value=top_role, inline=True)
    embed.add_field(name="Number of Roles", value=roles, inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Account Created on", value=created, inline=True)
    await ctx.channel.send(embed=embed)
    return


  @commands.command()
  async def quote(self, ctx):
    """
    This will trigger the bot to respond to the user with a random quote using zen quote API.

    >>>$quote
    {quote embedded}
    """
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = str(json_data[0]['q'] + ' -' + json_data[0]['a'])
    embed = discord.Embed(
      title = "Quote",
      description = quote,
      color = discord.Colour.blurple()
    )
    await ctx.channel.send(embed=embed)
    return


  @commands.command(aliases = ["profilepic"])
  async def pfp(self, ctx, member: discord.Member = None):
    """
    This will trigger the bot to respond with the user specified person's profile picture. If nothing specified, then return the sender's profile picture.
    """
    if member == None:
      await ctx.channel.send(ctx.author.avatar_url)
      return
    await ctx.channel.send(member.avatar_url)
    return


  @commands.command()
  async def iq(self, ctx):
    """
    This command send an embed of the user's IQ randomly.
    """
    the_iq = random.randrange(0,302)
    embed = discord.Embed(
      title = f"{ctx.author.name}'s IQ 🧠",
      description = f"**{the_iq}**",
      color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)
    return


def setup(bot):
  bot.add_cog(Fun(bot))
