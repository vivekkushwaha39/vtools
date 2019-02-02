'''
Created on 02-Feb-2019

@author: vivek_
'''
import xml.etree.ElementTree as ET

class IFSFRequestEditor:
    '''
    classdocs
    '''

    STATE_INIT, STATE_EDIT_START,STATE_ERROR, STATE_FINISH = 0,1,2,3

    def __init__(self, ifsfCommand):
        '''
        Constructor
        '''
        self.request = ifsfCommand
        self.status = IFSFRequestEditor.STATE_INIT
    
    def editInNpp(self):
        deviceInput = self.request.findATagByName(None, 'Input')
        insecDatas = self.request.findAllTagByName(deviceInput, 'InSecureData')
        
        for params in insecDatas:
            _, val, _ = self.request.getKeyVal(params)
        
        if val is not None:
            byte = bytearray.fromhex(val.text)
            val.text = byte
            
    def printXML(self):
        xmlString = self.request.genXMLString()
        print xmlString