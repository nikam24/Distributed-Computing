# Resumable File Transfer Server

The Resumable File Transfer Server is a Python-based server application that allows clients to download files and resume interrupted downloads from the point of interruption. It provides a convenient way to transfer files over a network connection while ensuring data integrity. If your client and server are on the same machine then we will be using the same loopback address ( 127.0.0.1 ) and port 5555 for communication. But if you want the server and client to be on separate machine's then just replace the ip address in both server and client code with the actual ip address of server machine ( This will work only if both client and server ) are on the same network.

## Features

- Resumable file transfers: Clients can pause and resume downloads.
- Error handling: Gracefully handles client disconnections and file not found errors.
- Easy to use: Simple server and client scripts for file transfer.

## Requirements

- Python 3.x

## Usage

### Server

1. Clone or download this repository to your server machine.

2. Open a terminal and navigate to the project directory.

3. Run the server script:

   ```shell
   python server.py

The server will start listening for incoming connections.

Client
Clone or download this repository to your client machine.

Open a terminal and navigate to the project directory.

Edit the client.py script to specify the server's IP address and port.

Run the client script:

shell
Copy code
python client.py
The client will connect to the server and initiate a file transfer. You can pause and resume the download as needed.

Configuration
You can customize the following settings in the server.py script:

host: The server's IP address or hostname.
port: The port number on which the server listens for connections.
file_path: The path to the file you want to serve to clients.
Contributing
If you'd like to contribute to this project, please open an issue or submit a pull request with your improvements or bug fixes.

License
This project is licensed under the PSN(Pratham Sanjay Nikam) License. See the LICENSE file ( that does not exist yet) for details.
