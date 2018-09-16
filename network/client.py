import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def SendMsg(addr, msg):
    socket_client.send(msg, addr)
    return s.recv(1024).decode('utf-8')
