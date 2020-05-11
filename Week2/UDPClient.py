
# Import the socket module for network communication
from socket import *
# Use localhost, so a DNS lookup will return the right IP address
serverName = 'localhost'
# Specify a port number for the connection to attach to
serverPort = 12000
# Create the socket, specifying that it is a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Display text to the console and prompt the user for input
message = input('Input lowercase sentence:') 
# Send message into the socket, after converting it to byte type
clientSocket.sendto(message.encode(), (serverName, serverPort)) 
# Retrieve the message from the server and its address
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
# Convert the byte type message into a string type
print(modifiedMessage.decode())
# Close the socket to end the process
clientSocket.close()
