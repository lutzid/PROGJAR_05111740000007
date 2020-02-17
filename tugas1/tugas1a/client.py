import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Transfer file
    file_name = input("enter file name that you want to send: ")
    try:
        # Open file
        f = open(file_name, 'rb')
    except:
        print("file can't be opened")
    else:
        length = f.read(1024)
        while length:
            sock.send(length)
            length = f.read(1024)
        f.close()
finally:
    print("closing")
    #close socket
    sock.close()