import socket
HOST = "127.0.0.1"
PORT = 12000

def tcp_server():
    sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sockServer.bind((HOST, PORT))

    sockServer.listen()

    print("Ready")

    while True:
        sockClient, clientAddr = sockServer.accept()

        request = sockClient.recv(1024).decode()
        print("From client :"+request)

        response = handleReq()
        sockClient.send(response.encode())

        sockClient.close()

    sockServer.close()

def handleReq():
    respone_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    file = open("files/ind.html", 'r')
    message_body = file.read()
    file.close()
    response = respone_line+content_type+message_body
    return response

if __name__ == "__main__":
    tcp_server()