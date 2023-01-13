"""
This file holds all the administrator commands.
Copyright (c) 2022 Mathavan Pirathaban
"""

from discord.ext import commands
import discord

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(aliases = ['del'])
  @commands.has_permissions(administrator = True)
  async def delete(self, ctx, limit = 5):
    """
    This will trigger the bot to delete the messages in the channel. Only the administrator can run this command and the limit can be set to any number. If no limit is provided, then the default will be 5 messages deleted. The bot will send an embed of the number of messages that were deleted.
    """
    users = []
    messages_sent = []
    messages = await ctx.channel.purge(limit = limit + 1)
    for msg in messages:
      if str(msg.author) in users:
        messages_sent[users.index(str(msg.author))] += 1
      else:
        users.append(str(msg.author))
        messages_sent.append(1)
    messages_sent[0] -= 1
    embed = discord.Embed(
      title = "Successfully deleted " + str(len(messages) - 1) + " messages!",
      color = discord.Colour.dark_gold()
    )
    for i in range(len(users)):
      embed.add_field(
        name = users[i],
        value = str(messages_sent[i]) + " Message(s) deleted",
        inline = False
      )
    await ctx.channel.send(embed = embed)
    return


  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx, member: discord.Member, *, reason = None):
    """
    This command will trigger the bot to kick out the specified user, member, from the server. Only the users with permission of kicking members from the server can successfully use the command.
    """
    if reason == None:
      reason = "No reason is provided."
    embed = discord.Embed(
      title = str(member) + " is kicked from the server 🦶",
      description = "Reason: " + str(reason),
      color = discord.Color.from_rgb(240, 2, 121)
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.guild.kick(member)
    await ctx.channel.send(embed=embed)
    return


  @commands.command()
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member: discord.Member, *, reason = None):
    """
    This command will trigger the bot to ban the member from the server. Only the users with banning members permission can successfully use this command.
    """
    if reason == None:
      reason = "No reason is provided."
    embed = discord.Embed(
      title = str(member) + " is banned from the server ❌",
      description = "Reason: " + str(reason),
      color = discord.Color.from_rgb(255, 0, 47)
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    await ctx.guild.ban(member)
    await ctx.channel.send(embed=embed)
    return


  @commands.command()
  @commands.has_permissions(ban_members = True)
  async def unban(self, ctx, *, member):
    """
    This command will trigger the bot to unban the member from the server. Only the users with banning members permission can successfully use this command.
    """
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    user = None
    for banned_user in banned_users:
      if (banned_user.user.name, banned_user.user.discriminator) == (member_name, member_discriminator):
        user = banned_user.user
    embed = discord.Embed(
      color = discord.Color.from_rgb(158, 147, 149)
    )
    if user == None:
      embed.title = "No user found 🤷‍♂️"
      await ctx.channel.send(embed=embed)
      return
    else:
      embed.title = str(user.name) + " is unbanned 🙌"
      embed.set_thumbnail(url=user.avatar_url)
    await ctx.guild.unban(user)
    await ctx.channel.send(embed=embed)
    return



async def setup(bot):
  await bot.add_cog(Admin(bot))
