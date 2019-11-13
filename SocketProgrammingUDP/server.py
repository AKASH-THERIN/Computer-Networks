from socket import socket

server_name = "localhost"
server_port = 8080
server_socket = socket()
server_socket.bind((server_name, server_port))
server_socket.listen()

while True:
    connection_socket, address = server_socket.accept()
    message = connection_socket.recv(2048)
    connection_socket.send(message.decode().upper().encode())
    print(message)
    connection_socket.close()
