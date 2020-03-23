import socket
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("put ")
    filename = input("enter filename: ")
    try:
        f = open(filename, 'rb')
    except:
        print("File Can't Be Open")
    else:
        file_content = base64.b64encode(f.read())
        f.close()
        f = open("temp","wb")
        f.write(file_content)
        f.close()
        f = open("temp","rb")
        request = command.encode() + filename.encode() + (b" ") + f.read(1024)
        print(request)
        while (request):
            sock.send(request)
            request = f.read(1024)
            response = sock.recv(1024)
        f.close()
        os.remove("temp")
finally:
    print("closing")
    sock.close()