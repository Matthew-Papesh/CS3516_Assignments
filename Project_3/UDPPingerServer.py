#please note that you only need to run the server on your local host, or on a different device on the same local network as the client. The wpi server will not allow you to have a port open for test. 

#We will need the following module to generate randomized lost packets 
import random
from socket import *

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
serverSocket = socket(AF_INET, SOCK_DGRAM)
print("socket created")
#Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 12000))
print("socket bound to port")

while True: 
    print('Ready to serve...')
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    print(rand)
    #Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
    print("xy_message:"+message.decode())
    print("xy_address:"+str(address))
    #decode the message first
    message=message.decode()
    #Capitalize the message from the client
    message = message.upper()
    print("xy_capitalized_message:"+message)
    #If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
    	continue
    #Otherwise, the server responds (need to encode the message before sending it)
    serverSocket.sendto(message.encode(), address)
 
