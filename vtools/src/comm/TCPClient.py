import socket
from vtools.src.comm.CommConfig import CommConfig
from time import sleep


class TCPClient:
    
    
    def __init__(self):
        self.client = None
        self.ipaddr = '192.168.31.126'
        self.port = 4000 
    
    def connect(self, ip, port):
        
        self.ipaddr = ip
        self.port = port
        
        ret = True
        try :
            self.client = socket.socket(socket.AddressFamily.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print(err)
            ret = False
        
        if  ret == False :
            return ret
        
        self.client.connect((self.ipaddr, self.port))
        
    
    def sendMsg(self, msg):
        
        byteData = msg.encode()
        
        intSize = len(byteData)
        
        bytesize = intSize.to_bytes(4, byteorder='big')
        
        bytePacket = bytearray(0)
        
        bytePacket.extend(bytesize)
        bytePacket.extend(byteData)
        
        print(bytePacket)
        
        sent = 0
        sent = self.client.send(bytePacket)
        
        print(sent, len(byteData))
        return sent
    
    def recvMsg(self):
        chunks = []
        chunk = self.client.recv(CommConfig.BUFF_SIZE)
        while ( chunk != b'' ):
            print(chunk)
            
            chunks.extend(chunk)
            chunk = self.client.recv(CommConfig.BUFF_SIZE)
            
        return chunks
    
    def disconnect(self):
        self.client.close()