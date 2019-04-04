import socket
from vtools.src.comm.CommConfig import CommConfig
from _socket import AF_INET, SOCK_STREAM


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
            self.client = socket.socket(AF_INET, SOCK_STREAM)
        except socket.error as err:
            print(err)
            ret = False
        
        if  ret == False :
            return ret
        
        self.client.connect((self.ipaddr, self.port))
        
    
    def sendMsg(self, msg):
        
        byteData = msg.encode()
        print(byteData)
        intSize = len(byteData)
        
        bytesize = TCPClient.intToByteArray(intSize)
        
        bytePacket = bytearray(0)
        
        bytePacket.extend(bytesize)
        bytePacket.extend(byteData)
        
        print(bytePacket)
        
        sent = 0
        sent = self.client.send(bytePacket)
        
        print(sent, len(byteData), bytesize)
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
    
    @staticmethod
    def intToByteArray(intData):
        return intData.to_bytes(4, 'big')
        
        strBytes = '%08X'%intData
        bytearr = bytearray(0)
        
        for i in range(0, len(strBytes), 2 ):
            currByte = chr(int(strBytes[i:i+2], 16))
            bytearr.extend(currByte)
        
        return bytearr