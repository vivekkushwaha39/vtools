'''
Created on 01-Feb-2019

@author: VivekK4
'''

class IFSFHandler:
    '''
    classdocs
    '''


    def __init__(self, ip='192.168.31.126', port = 4000):
        '''
        Constructor
        '''
        self.host = ip;
        self.port = port
        
    def processRequestString(self, req):
        
        