'''
Created on 02-Feb-2019

@author: vivek_
'''

import os
class FileHandler:
    '''
    A class for file manipulation of logs and commands
    '''
    

    def __init__(self, fileName, isFullPath=False):
        '''
        Constructor
        @param fileName: name of the file
        @param isFullPath: if false then temporary path will be used that is `tmp`
                environment variable
        
        '''
        if isFullPath == False:
            #TODO: write platform independent code
            tmpdirectory = os.environ['tmp']
            separator = "\\"
            self.fileName = tmpdirectory + separator + fileName
        else:
            self.fileName = fileName
        self.fileHandle = None
        
        
    def open(self):
        '''
        opens file handle only when it is needed
        @note: Don't forget to close file handle
        '''
        self.fileHandle = open(self.fileName)
        
    def close(self):
        if self.fileHandle is not None:
            self.fileHandle.close()
            self.fileHandle = None
        
    def writeText(self, text):
        '''
        write text into file
        @return: True if success otherwise error description
        '''
        
        if self.fileHandle is None:
            return 'File is not opened'
        
        self.fileHandle.write(text)
        return True
    
    def openWithEditor(self, editorCommandLine="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"):
        self.close()
        os.system(editorCommandLine + " " + self.fileName)
    
    def saveAs(self, destDir):
        self.close()
        os.system('cp ' + self.fileName + ' ' + destDir)
    
    
    
    def readAll(self):
        if self.fileHandle is None:
            return 1, 'File is not opened'
        
        text = self.fileHandle.read()
        return 0, text