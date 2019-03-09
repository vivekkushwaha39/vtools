'''
Created on 02-Feb-2019

@author: vivek_
'''
from vtools.src.comm.TCPClient import TCPClient
class POPCommunicator:
    '''
    classdocs
    '''


    def __init__(self, popIp, popPort):
        '''
        Constructor
        '''
        self.ip = popIp
        self.port = popPort
    
    def sendRequest(self, command):
        '''
        A function to send request and wait for response
        @author: Vivek Kushwaha <vivekkushwaha39@gmail.com>
        '''
        tcpcomm = TCPClient()
        tcpcomm.connect(self.ip, self.port)
        tcpcomm.sendMsg(command)
        response = tcpcomm.recvMsg()
        print ( response )
        return response
    
    def getPopIp(self):
        '''
        returns pop ip
        '''
        return self.ip
    
    def getPopPort(self):
        '''
        returns pop port
        '''
        return self.port