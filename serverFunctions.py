import json, socket, os
from wakeonlan import send_magic_packet


class serverFunctions():

    def clientToken(self):
        return (os.environ['DISCORD_TOKEN'])

    def minecraftRole(self):
        return(os.environ['MINECRAFT_ROLE'])

    def serverCheck(self, port):

        #open a socket connection with the location defined as the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        location = (os.environ['MINECRAFT_IP'],int(port))
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

    def wakeOnLAN(self):
        send_magic_packet(os.environ['SERVER_MAC'], ip_address = os.environ['MINECRAFT_IP'], port = int(os.environ['WOL_PORT']))

    def serverSocket(self):
        if (os.environ['test'] == '1'):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((os.environ['MINECRAFT_IP'], int(os.environ['PYTHON_SERVER_PORT'])))
                os.environ['test'] = '0'
                msg = s.recv(20)
                returnMessage = msg.decode('utf-8')
                s.close()
            except:
                returnMessage = 'Computer not started'
        else:
            returnMessage = 'The command has already been run. The server should be up'

        return(returnMessage)