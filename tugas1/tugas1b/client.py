import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    fname = input("enter file name and it's extension that you want to send: ")
    sock.send(fname.encode())

    file_name = 'received_file'
    with open(file_name, 'wb') as f:
        while True:
            data = sock.recv(1024)
            
            if not data:
                break
            # Write data to a file
            f.write(data)
    f.close()
except:
    print("error")

finally:
    print("closing")
    #Close socket
    sock.close()