import socket

client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_s.connect((socket.gethostname(),1234))

messsage = client_s.recv(1024)
print(messsage.decode("utf-8"))