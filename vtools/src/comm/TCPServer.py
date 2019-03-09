'''
Created on 01-Feb-2019

@author: VivekK4
'''
import socketserver
import  socket
from vtools.src.comm.CommConfig import CommConfig

class TCPServer:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.clientSock = None
        self.serverSock = None
        self.clientAddr = None
    
    def createSock(self, port=4000, host = ''):
        self.serverSock = socketserver.socket.socket(socket.AddressFamily.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((host, port))
        print("listening for devices")
        self.serverSock.listen(1)
        print("accepting")
        self.clientSock, _ =  self.serverSock.accept()
    
    def sendMsg(self):
        if ( self.clientSock is None ):
            return False
        
    def recvMsg(self):
        if ( self.clientSock is None ):
            return False
        
        chunks = []
        chunk = self.clientSock.recv(CommConfig.BUFF_SIZE)
        while ( chunk is not '' ):
            chunks.append(chunk)
            chunk = self.clientSock.recv(CommConfig.BUFF_SIZE)
        
        return ''.join(chunks)