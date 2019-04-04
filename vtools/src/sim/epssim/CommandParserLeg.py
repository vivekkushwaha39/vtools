'''
Created on 03-Feb-2019

@author: vivek_
'''

import xml.etree as ET
from vtools.src.sim.epssim.IFSFRequest import IFSFRequest
class CmdParserLeg:
    '''
    Legacy Command parser
    Old style which is made in java
    '''


    def __init__(self, fileName="vtools/res/cmdData.xml"):
        self.xmlDataRoot = ET.ElementTree.parse(fileName)
        cmdDatas = self.xmlDataRoot.findall('cmdData')
        # list of parsed request with key= "Commandname" value="IFSFRequestObject"
        self.requestList = {} 
        
        
        for cmdData in cmdDatas:
            ifsfreq = IFSFRequest('')
            ifsfreq.setCommand(cmdData[0])
            commandName=cmdData.attrib['name']
            self.requestList[commandName] = ifsfreq
    
    def getCommands(self):
        return self.requestList