# Import the socket module for network communication
from socket import *
# Specify a welcome port for the client to "shake hands" with
serverPort = 12000
# Create the welcome socket, specifying that it is a TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM) 
# Assign the port number to the server's welcome socket 
serverSocket.bind(('',serverPort)) 
# Wait for the client to initiate a TCP connection request
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    # Create a TCP connection for byte transfer between client and server
    connectionSocket, addr = serverSocket.accept() 
    # Retrieve and convert message from client from bytes to string
    sentence = connectionSocket.recv(1024).decode() 
    # Change the client message to uppercase
    capitalizedSentence = sentence.upper() 
    # Send the updated message back through the TCP connection to client
    connectionSocket.send(capitalizedSentence.encode()) 
    # Close this socket/connection, but keep the welcome socket open
    connectionSocket.close()
