import json, socket, os
from wakeonlan import send_magic_packet
import constants as const

class serverFunctions():


    def serverCheck(self, port):

        #open a socket connection with the location defined as the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        location = (const.MINECRAFT_IP,int(port))
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
        return('```' + 'Instructions: ' + const.INSTRUCTIONS_LINK + '```')

    def getDownload(self):
        return ('```' + 'Mods: ' + const.MOD_DOWNLOAD_LINK + '```')

    def wakeOnLAN(self):
        send_magic_packet(const.SERVER_MAC, ip_address = const.MINECRAFT_IP, port = const.PYTHON_SERVER_PORT)

    def serverSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((const.MINECRAFT_IP, const.PYTHON_SERVER_PORT))
            msg = s.recv(200)
            returnMessage = msg.decode('utf-8')
            s.close()
        except socket.timeout:
            returnMessage = 'Computer has not started'
        return(returnMessage)