#Mengimport socket
from socket import *

serverName = 'localhost'
# Menetapkan nomor port server
serverPort = 12000

# Membuat socket server
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# Menerima permintaan koneksi dari client
serverSocket.listen(1)
print('Server is Ready...')

while True:
    # Membuat koneksi antara client dan server
    connectionSocket, addr = serverSocket.accept()
    try:
        # Memasukkan data paket ke variabel message
        message = connectionSocket.recv(1024)
        filename = message.split()[1]

        # Membuka dan membaca file yang diminta client
        f = open(filename[1:], 'rb')
        outputdata = f.read()

        # Menutup file
        f.close()

        # Mengirim status code dan konten file yang diminta oleh client
        connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n' + outputdata)
        connectionSocket.close()

    except IOError:
        # Mengirim respons berupa status code apabila file tidak ditemukan
        response_header = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n'
        response_data = b'<html><body><h1>404 Not Found</h1><h3>The file you\'re looking for does not exist.</h3></body></html>'

        response = response_header.encode() + response_data
        connectionSocket.sendall(response)

        # Close client socket
        connectionSocket.close()

serverSocket.close()
