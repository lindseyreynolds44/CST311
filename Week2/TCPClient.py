# Import the socket module for network communication
from socket import *
# Use localhost, so a DNS lookup will return the right IP address
serverName = 'localhost'
# Specify a port number for the connection to attach to
serverPort = 12000
# Create the socket, specifying that it is a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM) 
# Initiate a TCP connection, with the serverName and "welcome" port number
clientSocket.connect((serverName,serverPort)) 
# Display text to the console and prompt the user for input
sentence = input('Input lowercase sentence:') 
# Send the user's input across the TCP connection in byte type
clientSocket.send(sentence.encode()) 
# Receive the changed message from the server through the TCP connection
modifiedSentence = clientSocket.recv(1024) 
# Print the new message to the console
print('From Server: ', modifiedSentence.decode()) 
# Close the socket and the connection and end the process
clientSocket.close()