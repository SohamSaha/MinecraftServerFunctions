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
async def startcomputer(ctx):
    code = 0
    PST = datetime.datetime.now().hour - 7 
    for i in ctx.author.roles:
        if (str(i.id) == str(os.environ['MINECRAFT_ROLE_ID'])):
            if (PST >= int(os.environ['SERVER_START_TIME']) or PST < int(os.environ['SERVER_END_TIME'])):
                code = 1
            else:
                errorCode = 'this command only works between 10 AM PST and 2 AM PST'
                break
        else:
            errorCode = 'you do not have the proper roles'

    if (code == 1):
        myServer.wakeOnLAN()
    elif (code == 0):
        await ctx.send('You cannot use this command because: ' + errorCode)

@client.command()
async def serverStart(ctx):
    await ctx.send(myServer.serverSocket())

@tasks.loop(seconds=60)
async def changeStatus():
    if (myServer.serverCheck(os.environ['MINECRAFT_PORT'])):
        await client.change_presence(status=discord.Status.online)
    else:
        await client.change_presence(status=discord.Status.offline)

client.run(myServer.clientToken())