import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # define socket
s.connect((socket.gethostname(), 5467)) # bind socket to localhost:5000

msg = s.recv(1024) # buffer size 1024
s.close()
print(msg.decode("utf-8"))