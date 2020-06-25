import discord, os
from serverFunctions import serverFunctions
from misc import misc
from discord.ext import commands, tasks
import datetime

client = commands.Bot(command_prefix = "!", case_insensitive=True)
client.remove_command('help')
myServer = serverFunctions()
miscFunctions = misc()

@client.event
async def on_ready():
    changeStatus.start()
    print ('Bot is ready.')

@client.event
async def onCommandError(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That is not a valid command. Type in !help to see all the commands')

@client.command(pass_context=True)
async def help(ctx):

    author = ctx.message.author

    embed = discord.Embed()

    embed.add_field(name ='!serverstatus', value = 'Returns server status', inline = False)
    embed.add_field(name ='!mods', value = 'Returns mod download', inline = False)
    embed.add_field(name ='!instructions', value = 'Returns installation instructions', inline = False)
    embed.add_field(name ='!download', value = 'Returns mod download folder', inline = False)
    embed.add_field(name ='!anjew', value = 'Returns a funny gif', inline = False)

    await author.send(embed=embed)

@client.command()
async def serverstatus(ctx):
    if (myServer.serverCheck(os.environ['MINECRAFT_PORT'])):
        await ctx.send('```' + 'Server is up' + '```')
    else:
        await ctx.send('```' + 'Server is down' + '```')

@client.command()
async def mods(ctx):
    await ctx.send(myServer.activeModList())

@client.command()
async def instructions(ctx):
    await ctx.send(myServer.installationInstructions())

@client.command()
async def download(ctx):
    await ctx.send(myServer.getDownload())

@client.command()
async def anjew(ctx):
    embed = discord.Embed()
    embed.set_image(url = miscFunctions.randomMenorah())

    await ctx.send(embed=embed)

@client.command()
@commands.has_role(myServer.minecraftRole())
async def roles(ctx):
    user = ctx.author
    await ctx.send(str(user) + 'checks fo the thing adn current time: ' + datetime.datetime.now().time())

@client.event
async def onRolesError(ctx, error):
    if isinstance(error, roles.MissingRole):
        await ctx.send('You do not have the proper role: ' + + datetime.datetime.now().time())

@tasks.loop(seconds=60)
async def changeStatus():
    if (myServer.serverCheck(os.environ['MINECRAFT_PORT'])):
        await client.change_presence(status=discord.Status.online)
    else:
        await client.change_presence(status=discord.Status.offline)


client.run(myServer.clientToken())