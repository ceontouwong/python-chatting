import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 21203
s.bind((host, port))

print("BINDED UDP ON "+ str(port))

def ServerOn():
    data, addr = s.recvfrom(1024)
    reply = "CONNECTED"
    s.sendto(reply.encode('utf-8'), addr)
    return data, addr
