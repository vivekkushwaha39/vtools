'''
Created on 02-Feb-2019

@author: vivek_
'''
import xml.etree.ElementTree as ET
from src.sim.epssim.IFSFRequest import IFSFRequest

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
        
        iccDatas = self.request.findAllTagByName(insecDatas[0], 'ICCData')
        
        for params in iccDatas:
            _, val, _ = self.request.getKeyVal(params)
            
            if val is not None:
                byte = bytearray.fromhex(val.text)
                val.text = str(byte)
        
    def printXML(self):
        xmlString = self.request.genXMLString()
        xmlString = IFSFRequest.prettyPrint(xmlString)
        print xmlString