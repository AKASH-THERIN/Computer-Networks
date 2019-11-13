from socket import socket

serverName ="10.124.6.83"
# serverName = "localhost"
serverPort = 8080
clientSocket = socket()
message = "hi.txt"
clientSocket.connect((serverName, serverPort))

clientSocket.send(message.encode())
filecontents, address = clientSocket.recvfrom(2048)
print("From server : ", filecontents.decode())
clientSocket.close()
