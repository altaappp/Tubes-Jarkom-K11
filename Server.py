# Import modul socket
import socket         

# Membuat fungsi serve_html
def serve_html(client_socket, filename):          
    try:     
        # Membuka file {filename} dengan mode 'r'           
        with open(filename, 'r') as file:
            # Membaca isi file dan mengisinya ke response_data
            response_data = file.read()
        # Membangun header respons HTTP 200 OK, konten sebagai HTML, dan panjang konten yang didapat
        response_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\n\r\n'.format(
            len(response_data))
        # Mengirim header respons ke soket klien setelah di encode menjadi byte
        client_socket.send(response_header.encode()) 
        # Mengirim response data ke soket klien setelah di encode menjadi byte     
        client_socket.send(response_data.encode())       
    # Menangkap kesalahan masukan jika terjadi
    except IOError:   
        # Membangun header respons HTTP 404 Not Found, konten sebagai HTML, dan panjang konten yang didapat          
        response_header = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 0\r\n\r\n'
        # Mengirim response data ke soket klien setelah di encode menjadi byte
        client_socket.send(response_header.encode())

def start_server():
    # Membuat soket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Menentukan alamat IP dan nomor port
    server_address = ('172.20.10.5', 12000)
    # Mengikat(bind) soket server ke alamat IP dan port
    server_socket.bind(server_address)     
    # Mengaktifkan mode listen pada soket server, dapat menerima 5 koneksi klien.
    server_socket.listen(5)    
    #Menampilkan pesan bahwa server sedang berjalan dan mendengarkan pada port 12000             
    print('Server is running on port 12000...')   
    
    # Memulai loop yang akan terus menerima koneksi klien
    while True:        
        # Menampilkan pesan bahwa server sedang menunggu koneksi                    
        print('Waiting for clients...')           
        # Menerima koneksi dari klien. Accept() akan memblokir eksekusi hingga ada koneksi yang diterima
        client_socket, client_address = server_socket.accept()      

        try:
            # Menampilkan pesan bahwa klien telah terhubung
            print('Client connected:', client_address)   
            # Menerima request dari klien yang terhubung melalui soket klien. Decode dari byte jadi string
            request = client_socket.recv(1024).decode()   
            #Menampilkan request dari klien
            print('Received request:', request)        

            request_lines = request.split('\r\n')        

            # Mendapatkan nama file dari request HTTP
            filename = request.split(' ')[1].lstrip('/')
            # Menampilkan nama file yang direquest
            print('Requested file:', filename)          

            # Mengirim file HTML ke klien dengan memanggil fungsi serve_html
            serve_html(client_socket, filename)          
        except Exception as e:
            print('Error:', str(e))

        # Menutup soket klien setelah melayani request
        client_socket.close() 
        # Menampilkan pesan               
        print('Client connection closed.')

    # Menutup soket server
    server_socket.close()           

if __name__ == '__main__':
    start_server()
