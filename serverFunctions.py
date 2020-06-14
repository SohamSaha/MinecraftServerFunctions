import constants
import json
import socket


class serverFunctions():

    def clientToken(self):
        return (os.environ['DISCORD_TOKEN'])

    def serverCheck(self):

        #open a socket connection with the location defined as the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        location = (os.environ['IP'],int(os.environ['PORT']))
        check=s.connect_ex(location)

        #if the port is open and listening, show that the server is up
        if (check ==0):
            return('```' + 'Server is up' + '```')
        else:
            return ('```' + 'Server is down' + '```')

        #close the socket connection
        s.close()

    def activeModList(self):

        modList = []
        #Read the JSON file in and then close the file
        file = open('mods.json') 
        with file as f:
            data = json.load(f)
        file.close()
        
        #Iterate through the mod list and only return whichever mods are currently labelled as active
        for mod in data['Mods']:
            if (mod['active'] == 'true'):
                modList.append(mod['name'])

        return ('```' + '\n'.join(modList) + '```')

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