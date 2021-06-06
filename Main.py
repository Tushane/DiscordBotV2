import discord
from discord.ext import commands

Token = 'ODUwODc1MTY2NzY1MzUwOTEy.YLwFQA.PY7CJqM31RsalaDapfDXUXZufls'

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Sara is Live')


@client.event
async def on_member_join(member):
    return

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.command()
async def add_my_role(ctx, user_type):

    user: discord.Member = ctx.author
    role: discord.Role

    if (user_type == 'con'):
        role = discord.utils.get(ctx.guild.roles, name = 'content-creators')
    elif(user_type == 'sub'):
        role = discord.utils.get(ctx.guild.roles, name = 'subscribers')

    await user.add_roles(role)

    await ctx.send(f'Your Role has been Added. Hope You Enjoy Your Stay! {ctx.author.mention}')


client.run(Token)

