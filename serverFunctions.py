import json, socket, os


class serverFunctions():

    def clientToken(self):
        return (os.environ['DISCORD_TOKEN'])

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
            return True
        else:
            return False

    def activeModList(self):
        
        return ('```The server is currently using Valhesia 2 Modpack. Please take a look at installation instructions to see how to install```')

    def installationInstructions(self):

        return('```' + 'Instructions: https://drive.google.com/file/d/1w2NQBrxDBNafMEOG2HMsFO25I-WJGHHF/view?usp=sharing' + '```')

    def getDownload(self):

        return ('```' + 'Mods: https://drive.google.com/file/d/1Rv0eodZw60ozQ59kFbEkNt7GQxg5V4T6/view?usp=sharing' + '```')