'''
Created on 02-Feb-2019

@author: vivek_
'''
import xml.etree.ElementTree as ET
from vtools.src.sim.epssim.IFSFRequest import IFSFRequest
from vtools.src.utils.FileHandler import FileHandler


class IFSFRequestEditor:
    '''
    classdocs
    '''

    STATE_INIT, STATE_EDIT_START, STATE_ERROR, STATE_FINISH = 0, 1, 2, 3

    def __init__(self, ifsfCommand):
        '''
        Constructor
        '''
        self.request = ifsfCommand
        self.status = IFSFRequestEditor.STATE_INIT
        self.editingFile = None
    
    def decodeInsecureData(self):
        deviceInput = self.request.findATagByName(None, 'Input')
        
        insecDatas = self.request.findAllTagByName(deviceInput, 'InSecureData')
        
        for insecData in insecDatas:
            iccDatas = self.request.findAllTagByName(insecData, 'ICCData')
            
            print (len(iccDatas))
            for params in iccDatas:
                _, val, _ = self.request.getKeyVal(params)
                
                if val.text is not None:
                    val.text = val.text.decode('hex')
    
    def encodeInsecureData(self):
        deviceInput = self.request.findATagByName(None, 'Input')
        
        insecDatas = self.request.findAllTagByName(deviceInput, 'InSecureData')
        
        for insecData in insecDatas:
            iccDatas = self.request.findAllTagByName(insecData, 'ICCData')
            
            print (len(iccDatas))
            for params in iccDatas:
                _, val, _ = self.request.getKeyVal(params)
                
                if val.text is not None:
                    val.text = val.text.encode('hex')

    
    def editForAID(self, aid):
        self.request.selectInsecureData('9F06', aid)
    
    def editInNpp(self):
        self.decodeInsecureData()
        xmlfile = FileHandler('tmpCommand.xml')
        xmlfile.open()
        xmlfile.writeText(self.getXMLString())
        xmlfile.close()
        xmlfile.openWithEditor()
        self.editingFile = xmlfile
        
    def getXMLString(self):
        xmlString = self.request.genXMLString()
        xmlString = IFSFRequest.prettyPrint(xmlString)
        return xmlString
        
    def printXML(self):
        xmlString = self.request.genXMLString()
        xmlString = IFSFRequest.prettyPrint(xmlString)
        print ( xmlString )
        
    def convertHexStrToAscii(self, stringData):
        return stringData.decode('hex')
    
    def refreshFromEditedFile(self):
        if self.editingFile is None:
            raise Exception('No files being edited currently')
        
        self.editingFile.open('r')
        _, strData = self.editingFile.readAll()
        self.editingFile.close()
        self.request.parse(strData)
        self.encodeInsecureData()
        self.printXML()
        