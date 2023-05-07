 from socket import *

serverName = 'localhost'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is Ready...')

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], 'rb')
        outputdata = f.read()
        f.close()
        # Send the HTTP status code and content of the requested file to the client
        connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n' + outputdata)
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        response_header = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n'
        response_data = b'<html><body><h1>404 Not Found</h1><</body></html>'
        
        response = response_header.encode() + response_data
        connectionSocket.sendall(response)

        # Close client socket
        connectionSocket.close()

serverSocket.close()
