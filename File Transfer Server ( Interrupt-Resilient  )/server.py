# All code in this file is written by me i.e. pratham nikam, except for the code in the try block. Lol 😁
# Description: Server that sends a file to the client.
import socket
import time
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5555

server_socket.bind((host, port))
server_socket.listen()

server_socket.settimeout(5)

print(f"Server is listening at {host}:{port}")

while True:
    print("Waiting for client...")
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client at {client_address}")
        sended_bytes = client_socket.recv(1024).decode('utf-8')
        sended_bytes = int(sended_bytes)

        file_path = 'confidential.txt'
        file_size = os.path.getsize(file_path)
        
        print(f"Client requested to send {file_size-sended_bytes} bytes")

        try:
            with open(file_path, 'rb') as file:
                file.seek(sended_bytes)
                data = file.read(1024)
                while data:
                    try:
                        client_socket.send(data)
                        sended_bytes += len(data)
                    except ConnectionAbortedError:
                        print("Client disconnected.")
                        break

                    time.sleep(2) 
                    data = file.read(1024)
                time.sleep(2)  
            if sended_bytes == file_size:
                print(f"File '{file_path}' sent successfully")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

        client_socket.close()
    except socket.timeout:
        print("Server timed out.")
        break
    except KeyboardInterrupt:
        print("Server interrupted by user.")
        break

server_socket.close()
