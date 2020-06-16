import json, socket, os


class serverFunctions():

    def clientToken(self):
        return (os.environ['DISCORD_TOKEN'])

    def serverCheckLoop(self):
        #open a socket connection with the location defined as the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        location = (os.environ['MINECRAFT_IP'],int(os.environ['MINECRAFT_PORT']))
        check=s.connect_ex(location)

        #Close the socket connection
        s.close()

        if (check == 0):
            return True
        else:
            return False

    def serverCheck(self):

        #open a socket connection with the location defined as the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        location = (os.environ['MINECRAFT_IP'],int(os.environ['MINECRAFT_PORT']))
        check=s.connect_ex(location)

        #close the socket connection
        s.close()

        #if the port is open and listening, show that the server is up
        if (check == 0):
            return('```' + 'Server is up' + '```')
        else:
            return ('```' + 'Server is down' + '```')

    def activeModList(self):
        
        return ('```The server is currently using Valhesia 2 Modpack + ProjectE on Minecraft 1.15.2```')

    def installationInstructions(self):

        #Read the JSON file in and then close the file
        file = open('mods.json') 
        with file as f:
            data = json.load(f)
        file.close()
        
        #Iterate through the mod list and return the installation instruction
        for instruction in data['Documents']:
            if (instruction['name'] == 'Installation Guide'):
                return ('```' + instruction['link'] + '```')

    def getDownload(self):

        return ('``` \n' + 'Twitch Client: https://www.twitch.tv/downloads \n' + 'ProjectE: https://www.curseforge.com/minecraft/mc-mods/projecte ```')