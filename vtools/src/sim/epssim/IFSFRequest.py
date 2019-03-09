'''
Created on 01-Feb-2019

@author: vivek_
'''
import xml.etree.ElementTree as ET
import re


class IFSFRequest:
    '''
    A class to store IFSF requests and responses
    '''

    def __init__(self, reqStr):
        '''
        Constructor
        '''
        self.requestStr = reqStr
        self.requestXML = None
        self.currIccData = None
        self.currInSecureData = None
        self.namespace = '{http://www.nrf-arts.org/IXRetail/namespace}'
        ET.register_namespace('', 'http://www.nrf-arts.org/IXRetail/namespace')
        
    def parse(self, newRequestString=None):
        
        if newRequestString is not None:
            self.requestStr = newRequestString
        
        self.requestXML = ET.fromstring(self.requestStr)
        
    def setCommand(self, parsedCommand):
        self.requestXML=parsedCommand
    
    # get values from currently selected insecure data
    def getValFromCurrInsecData(self, tagName):
    
        returnVal = None
        if  self.currInSecureData is None :
            return None
        
        for params in self.currInSecureData:
            key, val, _ = self.getKeyVal(params)
            if key.text == tagName:
                returnVal = val
                break
        
        # TODO: need to encode before sending
        self.currIccData = params
        return returnVal

    def getKeyVal(self, rootIccData):
        currKey = None
        currVal = None
        
        for child in rootIccData:
            if child.tag == (self.namespace + 'ICCParameter') or (child.tag == self.namespace + 'SecureTag') :
                currKey = child 
            else:
                currVal = child
    
        return (currKey, currVal, child)
    
    def selectInsecureData(self, tag, value):   
        inputTag = self.findATagByName(self.requestXML, 'Input')
                    
        if inputTag is None:
            raise Exception('No input found')
        
        insecDatas = self.findAllTagByName(inputTag, 'InSecureData')
        
        found = False
        for insecData in insecDatas:
            for params in insecData:
                key, val, _ = self.getKeyVal(params)          
                if tag == key.text and value == val.text:
                    found = True
                    break
            
            if found == True:
                self.currInSecureData = insecData
                break
            
        if found == False:
            raise Exception('Tag `{0}` having value `{1}` Not found'.format(tag, value))
        
        return True
    
    def selectInsecureDataByIndex(self, index):
        try:
            inputTag = self.findATagByName(self.requestXML, 'Input')
            print(inputTag)
            if inputTag is None:
                raise Exception('No input found')
            
            insecDatas = self.findAllTagByName(inputTag, 'InSecureData')
            if len(insecDatas) < (index + 1):
                raise Exception('Insec data index not found ', index)
            self.currInSecureData = insecDatas[index]
             
        except Exception :
            print('error', Exception)
            return None
            
        return True
    
    def genXMLString(self):
        xmlString = ET.tostring(self.requestXML, 'utf-8', 'xml').decode()
        return xmlString

    def getResults(self):
        print("TODO: need to send results")
    
    def findATagByName(self, root, tagname):
        if root is None:
            root = self.requestXML
        
        return root.find(self.namespace + tagname)
    
    def findAllTagByName(self, root, tagname):
        if root is None:
            root = self.requestXML
            
        return root.findall(self.namespace + tagname)
    
    @staticmethod
    def prettyPrint(stringdata):
        return re.sub('>\s*<', ">\n<" , stringdata)
