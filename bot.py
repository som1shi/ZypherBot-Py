import discord
from discord.ext import commands
import random


description = '''The Ultimate Administration bot for your server. Your server is now on your fingertips! '''

bot = commands.Bot('!-- ', description=description)

@bot.event #This is what is printed when the bot is switched on
async def on_ready():
    print('The bot is active')

@bot.command() #This command prints the ping of the bot
async def ping(ctx):
    ping = round(bot.latency*1000)
    await ctx.send(f"The ping of this bot is {ping} ms")

@bot.command() #This command does a toss to carry out probalbilty
async def toss(ctx):
    responses = ['Heads', 'Tails']
    await ctx.send(f"The coil flip's result is **{random.choice(responses)}**")

@bot.command() #This command clears the previous {Specified} messages plus itself
async def clear(ctx, amount=5):
    amount = amount + 1
    upperLimit = 101
    if amount > upperLimit:
        await ctx.send("```Clears cannot excced 100```")

    if upperLimit >= amount:
        await ctx.channel.purge(limit=amount)


@bot.command() #This command kicks ppl
async def kick(ctx, member: discord.Member, reason=None):
    if reason == None:
        await ctx.send("```Please specify reason! !kick <User> <Reason>```")
    else:
        await member.kick()
        await ctx.send(f"```Successfully kicked {member} for {reason}```")

@bot.command() #This command bans ppl
async def ban(ctx, member: discord.Member, reason=None):
    if reason == None:
        await ctx.send("```Please specify reason! !ban <User> <Reason>```")
    else:
        await member.ban()
        await ctx.send(f"```Successfully banned {member} for {reason}```")

@bot.command() #This command unbans ppl
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = str.split("#")

    for banned_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.guild.send(f'```Successfully unbanned {user.name}#{user.discriminator}```')
            return

bot.run(token)

