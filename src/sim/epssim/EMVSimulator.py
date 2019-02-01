'''
Created on 01-Feb-2019

@author: VivekK4
'''

class EMVSimulator:
    '''
    a class to automate EMV Process
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.isEMVInitialized = False
        self.setIccConfigXML = None
        self.UpdateAIDXML = None
        self.UpdateKeysXML = None
        self.UpdateAIDRules = None
        self.ReadCard = None
    
    def initializeEMV(self):
        print("Initializing emv")
    
    def reloadCommandsFromXML(self):
        print("reading commands from xml")