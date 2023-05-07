# Mengimport socket
import socket

HOST = 'localhost'
# Menetapkan nomor port
PORT = 12000

# Meminta input nama file yang diinginkan kepada client
filename = input("Enter file name: ")
request = f"GET /{filename} HTTP/1.0\r\nHost: {HOST}\r\n\r\n"

# Membuat socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    # Mengirim permintaan GET ke server
    client_socket.sendall(request.encode('utf-8'))
    
    # Menerima respon dari server
    response = client_socket.recv(1024)
    
    # Output ketika tidak ada respon
    if not response:
        print("No response from the server.")
    else:
        # Parse HTTP response
        response_parts = response.split(b'\r\n\r\n')
        if len(response_parts) < 2:
            print("Invalid response from the server.")
        else:
            status_code, content = response_parts[0], response_parts[1]
            if status_code == b'HTTP/1.0 200 OK': 
                # Menyimpan file ke local directory
                with open(f"path\\{filename}", 'wb') as f:
                    f.write(content)
                print(f"File '{filename}' saved to the local directory.")
            else:
                print("File not found on the server.")
