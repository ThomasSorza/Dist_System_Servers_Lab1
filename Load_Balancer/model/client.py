import socket

HOST = input("Enter the add to connect: ")
PORT = 446 #port to connect

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object as INET ipv4 and TCP socket
socket.connect((HOST, PORT)) #connect to the server

socket.send(bytes(input("Enter Message to the server"), "utf-8")) #send a message to the server
print(socket.recv(1024).decode('utf-8')) #receive the message from the server

#socket basico (crear clase cliente que herede de socket.socket)