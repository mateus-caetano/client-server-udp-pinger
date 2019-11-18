from socket import *
from datetime import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)

i = 1

while (i <= 10):
    try:
        now = datetime.now()
        hour = now.strftime('%H:%M')
        clientSocket.settimeout(1)
        message = ("ping " + str(i) + " " + str(hour))
        clientSocket.sendto((message),('localhost', 12000))
        i += 1
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

    except timeout:
        print('Solicitacao expirada')

    else:
        print(modifiedMessage)

clientSocket.close()