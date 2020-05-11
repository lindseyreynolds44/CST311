
# Import the socket module for network communication
from socket import *
# Specify a port number for the connection to attach to
serverPort = 12000
# Create the socket, specifying that it is a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign the port number to the server's socket 
serverSocket.bind(('', serverPort)) 
print("The server is ready to receive") 
# The server enters a while loop to indefinitely receive packets
while True:
    # Retrieve the message and IP address/port number from the client
    message, clientAddress = serverSocket.recvfrom(2048) 
    # Convert the message from bytes to strings and then to uppercase
    modifiedMessage = message.decode().upper() 
    # Send a packet containing the message and client address to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
