import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    file_name = connection.recv(1024)
    print(file_name.decode())

    with open(file_name.decode(), 'rb') as file:
        connection.sendfile(file, 0)
    file.close()

    # Clean up the connection
    connection.close()