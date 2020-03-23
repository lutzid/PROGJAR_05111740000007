import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("download ")
    filename = input("enter filename: ")
    f = open(filename, 'wb')

    request = command.encode() + filename.encode()
    sock.send(request)
    data = sock.recv(1024)
    
    temp_file = (b"")
    while True:
        temp_file = temp_file + data
        if sys.getsizeof(data) != 1057:
            break
        else :
            data = sock.recv(1024)
    temp_file = base64.b64decode(temp_file)
    f.write(temp_file)
    f.close()
finally:
    print("closing")
    sock.close()