# All code in this file is written by me i.e. pratham nikam, except for the code in the try block. Lol 😁
# Description: Client that receives a file from the server.
import socket
import os
import sys  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5555

try:
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    file_path = 'received_file.txt'
    received_size = 0

    try:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            client_socket.send(str(file_size).encode('utf-8'))  
            received_size = file_size
        else:
            client_socket.send(b'0')  
            received_size = 0

        with open(file_path, 'ab') as file: 
            data = client_socket.recv(1024)
            while data:
                file.write(data)
                received_size += len(data)
                data = client_socket.recv(1024)
        print(f"File received and saved as '{file_path}' (Total Bytes Received: {received_size})")
    except Exception as e:
        print(f"Error receiving file: {str(e)}")

    client_socket.close()
except KeyboardInterrupt:
    print("Client interrupted by user.")
    client_socket.close()
    sys.exit(0)
