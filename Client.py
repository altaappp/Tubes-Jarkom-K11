# Import modul soket
import socket                     

def receive_html(server_socket):  
    # Membuat variabel dengan nilai awal byte kosong
    response_data = b""     
    # Memulai loop      
    while True:       
        # Menerima data dari soket server dengan ukuran buffer 1024 byte          
        data = server_socket.recv(1024)   
        # Memeriksa apakah data yang diterima kosong
        if not data:      
            # Jika kosong, loop berhenti          
            break             
        # Menggabungkan data yang diterima ke response_data
        response_data += data    

    # Mengembalikan response_data setelah di decode dari byte menjadi string
    return response_data.decode()     
    
def save_html(filename, response_data):
    # Membuka file(filename) dalam mode tulis 'w'
    with open(filename, 'w') as file:   
        # Menulis response_data ke dalam file  
        file.write(response_data)       

def start_client():
    # Menetapkan alamat IP dan port yang digunakan
    server_address = ('172.20.10.5', 12000)   

    # Mulai loop
    while True:        
        # Membuat soket klien           
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
        # Membuat koneksi ke server dengan IP dan port
        client_socket.connect(server_address)      
        # Menerima input berupa file HTML, q untuk quit         
        filename = input("Masukkan nama file HTML yang ingin di-request (tekan 'q' untuk keluar): ")    
        if filename.lower() == 'q':   
            break

        # Membuat request HTTP dengan metode GET untuk mengambil HTML, termasuk alamat IP server
        request = "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(filename, server_address[0])   
        # Mengirim request ke server setelah di encode menjadi byte   
        client_socket.send(request.encode())        

        # Menerima respons dari server dengan fungsi receive_html
        response = receive_html(client_socket) 
        # Menampilkan respons dari server     
        print("Response:")      
        print(response)           
        
        # Kondisi jika file ditemukan
        if response.startswith("HTTP/1.1 200"):             
            save_html(filename, response)
            # Maka akan disave dalam local directory
            print(f"File '{filename}' saved to the local directory.")  
        #Kondisi jika file tidak ditemukan   
        else:       
            print(f"File '{filename}' not found on the server.")      

    # Menutup soket klien
    client_socket.close()       

if __name__ == '__main__':
    start_client()
