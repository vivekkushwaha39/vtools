'''
Created on 01-Feb-2019

@author: vivek_
'''
import xml.etree.ElementTree as ET
from __builtin__ import Exception, None
from decimal import val

class IFSFRequest:
    '''
    classdocs
    '''


    def __init__(self, reqStr):
        '''
        Constructor
        '''
        self.requestStr = reqStr
        self.requestXML = None
        self.currIccData = None
        self.currInSecureData = None
        self.parse()
        
    def parse(self):
        self.requestXML = ET.fromstring(self.requestStr)


    # get values from currently selected insecure data
    def getValFromCurrInsecData(self, tagName):
    
        returnVal = None
        if  self.currInSecureData is None :
            return None
        
        for params in self.currInSecureData:
            key, val = self.getKeyVal(params)
            if key == tagName:
                returnVal = val
                break
        
        # TODO: need to encode before sending
        self.currIccData = params
        return returnVal


    def getKeyVal(self, rootIccData):
        currKey = None
        currVal = None
        
        for child in rootIccData:
            if child.tag == 'ICCParameter' or child.tag == 'SecureTag' :
                currKey = child.text 
            else:
                currVal = child.text
    
        return (currKey, currVal, child)
    
    def selectInsecureData(self, tag, value):
       
        try:
            inputTag = self.find('Input')
                        
            if inputTag is None:
                raise Exception('No input found')
            
            insecDatas = inputTag.findall('InSecureData')
            
            found = False
            for params in insecDatas:
                
                key, val = self.getKeyVal(params)            
                if tag == key and value == val:
                    found = True
                    break
            
            if found == False:
                raise Exception('Not found')
        except:
            print("Error")
            self.currInSecureData = None
            return False
        
        return True
    
    def selectInsecureDataByIndex(self, index):
        try:
            inputTag = self.find('Input')
                        
            if inputTag is None:
                raise Exception('No input found')
            
            insecDatas = inputTag.findall('InSecureData')
            if len(insecDatas) < (index+1):
                raise Exception('Insec data index not found ', index)
            self.currInSecureData = insecDatas[index]
            
        except:
            print('error')
            return None
            
        return True
            
    def getResults(self):
        print("TODO: need to send results")
    
    def findATagByName(self, root, tagname):
        node = None
        for child in root:
            if tagname == child.tag:
                node = child
                break
        return node
    
    def findAllTagByName(self, root, tagname):
        nodes = []
        
        for child in root:
            if tagname == child.tag:
                nodes.append( child )
        
        return nodes