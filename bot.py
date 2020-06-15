import discord
from serverFunctions import serverFunctions
from discord.ext import commands

client = commands.Bot(command_prefix = "!")
client.remove_command('help')
myServer = serverFunctions()

@client.event
async def on_ready():
    changeStatus.start()
    print ('Bot is ready.')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That is not a valid command. Type in !help to see all the commands')

@client.command(pass_context=True)
async def help(ctx):

    author = ctx.message.author

    embed = discord.Embed()

    embed.add_field(name='!ping', value = 'Returns server status', inline=False)
    embed.add_field(name='!mods', value = 'Returns active server mods', inline=False)
    embed.add_field(name='!instructions', value = 'Returns installation instructions', inline=False)
    embed.add_field(name='!download', value = 'Returns download link of selected mod', inline=False)

    await author.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(myServer.serverCheck())

@client.command()
async def mods(ctx):
    await ctx.send(myServer.activeModList())

@client.command()
async def instructions(ctx):
    await ctx.send(myServer.installationInstructions())

@client.command()
async def download(ctx, arg):
    await ctx.send(myServer.getDownload(arg))

@download.error
async def downloadError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('``` You forgot to select a mod to download ```')

@tasks.loop(seconds=60)
async def changeStatus():
    if (myServer.serverCheckLoop()):
        await client.change_presence(activity=discord.Game('hi'))

client.run(myServer.clientToken())