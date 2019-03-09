'''
Created on Mar 8, 2019

@author: VivekK4
''' 
from vtools.src.comm.TCPServer import TCPServer
class MX9Logger:
    '''
    classdocs
    '''


    def __init__(self, loggingFile=None):
        '''
        Constructor
        '''
        if ( loggingFile is None ):
            self.loggingFileName = 'mx9_log.log'
        else :
            self.loggingFileName = loggingFile
        
        self.stopProcess = False
        
    def startLogging(self):
        self.serverSock = TCPServer()
        try:
            self.serverSock.createSock(5678, '192.168.31.202')
            self.logFile = open(self.loggingFileName, mode='w')
        except Exception :
            print( Exception )
        
        while self.stopProcess == False :
            stringData = self.serverSock.recvMsg()
            self.logFile.write(stringData)
        
        self.logFile.close()
    