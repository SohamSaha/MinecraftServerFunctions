import discord, os, datetime
import constants as const
from serverFunctions import serverFunctions
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = "!", case_insensitive=True)
client.remove_command('help')
myServer = serverFunctions()

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

    await author.send(embed=embed)

@client.command()
async def serverstatus(ctx):
    if (myServer.serverCheck(const.MINECRAFT_PORT)):
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
async def startcomputer(ctx):
    code = 0
    for i in ctx.author.roles:
        if (str(i.id) == const.MINECRAFT_ROLE_ID):
            if (datetime.datetime.now().hour >= const.SERVER_START_TIME) or datetime.datetime.now().hour < (const.SERVER_END_TIME):
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

@tasks.loop(seconds=60)
async def changeStatus():
    if (myServer.serverCheck(const.MINECRAFT_PORT)):
        await client.change_presence(status=discord.Status.online)
    else:
        await client.change_presence(status=discord.Status.offline)

client.run(const.DISCORD_TOKEN)