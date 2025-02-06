#Programming Assignment 1B: Web Server

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) # tcp connection

# prepare a server socket
# define host name and network entry port:
host = "127.0.0.1"
port = 5342
# establish the connection
print ('Ready to serve...')
serverSocket.bind((host, port))
serverSocket.listen()

while True: # spin while running server
    # confirm connection
    connectionSocket, addr = serverSocket.accept()

    try:
        # receive 1024-bit buffer msg
        message = connectionSocket.recv(1024).decode()
        if message: # only read if a msg was sent
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            print(outputdata)
            # send one HTTP header line into socket
            responseHeader = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            response = responseHeader.encode() + outputdata.encode()
            connectionSocket.sendall(response)

        # send the content of the requested file to the client
        #for i in range(0, len(outputdata)):
        #    connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        # send response message for file not found
        responseHeader = "HTTP/1.1 404 Not Found\r\n\r\n404 Not Found"
        connectionSocket.sendall(responseHeader.encode())
        # close client socket
        connectionSocket.close()
        
# shut down the server 
serverSocket.close()
