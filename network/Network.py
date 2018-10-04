import socket
import thread
import time

class net():
    def __init__(self):
        self.serverSoc = None
        self.serverStatus = 0
        self.buffsize = 1024
        self.allClients = {}
        self.counter = 0

        self.name = "SDH"
        self.serverIP = "127.0.0.1"
        self.serverPort = 8090
        self.clientIP = "127.0.0.1"
        self.clientPort = 8091

    def handleSetServer(self):
        if self.serverSoc != None:
            self.serverSoc.close()
            self.serverSoc = None
            self.serverStatus = 0
        server_addr = (self.serverIP, self.serverPort)
        try:
            self.serverSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSoc = bind(server_addr)
            self.serverSoc.listen(5)
            self.INFO("Server Listening on %s:%s" % server_addr)
            thread.start_new_thread(self.lisenClients, ())
            self.serverStatus = 1
            if self.name == '':
                self.name = "%s:%s" % server_addr
        except:
            self.INFO("Error Setting up server.")

    def listenClient(self):
        while True:
            clientSoc, clientAddr = self.serverSoc.accept()
            self.INFO("Client connected from %s:%s" % clientAddr)
            self.addClient(clientSoc, clientAddr)
            thread.start_new_thread(self.handleClientMessage, (clientSoc, clientAddr))
        self.serverSoc.close()

    def handleAddClient(self):
        if self.serverStatus == 0:
            self.INFO("Set server address first")
            return
        clientAddr = (self.clientIP, self.clientPort)
        try:
            clientSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSoc.connect(clientAddr)
            self.INFO("Connected to client on %s:%s" % clientAddr)
            self.addClient(clientSoc, clientAddr)
            thread.start_new_thread(self.handleClientMessage, (clientSoc, clientAddr))
        except:
            self.INFO("Error connecting to Client on %s:%s" % clientAddr)

    def handleClientMessages(self, clientSoc, clientAddr):
        while True:
            try:
                data = clientSoc.recv(self.buffsize)
                if not data:
                    break
                self.addChat("%s:%s" % clientAddr, data)
                clientSoc.close()
                self.INFO("Client disconnected from %s:%s" % clientAddr)

    def handleSendChat(self, msg):
        #TODO
        if self.serverStatus == 0:
            self.INFO("Set Server address first")
            return "Set Server addr first"
        self.addChat(msg)

        pass

    def addChat(self,msg):
        #TODO

        pass

    def removeClient(self, clientSoc, clientAddr):
        print(self.allClients)
        del self.allClients[clientSoc]
        print(self.allClients)

    def INFO(self, msg):
        print("["+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime() ) + "]:" + msg)
