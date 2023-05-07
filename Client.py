import socket

HOST = 'localhost'
PORT = 12000

filename = input("Enter file name: ")
request = f"GET /{filename} HTTP/1.0\r\nHost: {HOST}\r\n\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    # Send the GET request to the server
    client_socket.sendall(request.encode('utf-8'))
    
    # Receive the response from the server
    response = client_socket.recv(1024)
    
    if not response:
        print("No response from the server.")
    else:
        # Parse the HTTP response
        response_parts = response.split(b'\r\n\r\n')
        if len(response_parts) < 2:
            print("Invalid response from the server.")
        else:
            status_code, content = response_parts[0], response_parts[1]
            if status_code == b'HTTP/1.0 200 OK':
                # Save the file to the local directory
                with open(f"C:\\Users\\LENOVO\\Documents\\TPL\\{filename}", 'wb') as f:
                    f.write(content)
                print(f"File '{filename}' saved to the local directory.")
            else:
                print("File not found on the server.")
