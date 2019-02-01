'''
Created on 01-Feb-2019

@author: VivekK4
'''
from xml.sax.xmlreader import XMLReader
from xml.etree.ElementTree import ElementTree

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
        
                