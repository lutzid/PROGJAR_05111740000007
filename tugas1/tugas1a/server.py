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

    # Receive file
    with open('received_file', 'wb') as f:
        while True:
            data = connection.recv(1024)
            
            if not data:
                break
            # Write data to a file
            f.write(data)
    f.close()

    # Clean up the connection
    connection.close()