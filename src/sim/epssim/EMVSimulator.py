'''
Created on 01-Feb-2019

@author: VivekK4
'''

from src.sim.epssim.IFSFRequest import IFSFRequest
from src.sim.epssim.POPCommunicator import POPCommunicator

class EMVSimulator:
    '''
    a class to automate EMV Process class can do following thing 
    1. initialize EMV
    2. send read card request
    3. Detect failure in response
    '''

    SETICCCONFIG = 'SetICCConfig'
    UPDATEAID = 'UpdateAID'
    UPDATEKEYS = 'UpdateKeys'
    UPDATEAIDRUEES = 'UpdateAIDRules'

    def __init__(self):
        '''
        Constructor
        '''
        self.isEMVInitialized = False
        self.setIccConfigXML = None
        self.UpdateAIDXML = None
        self.UpdateKeysXML = None
        self.UpdateAIDRulesXML = None
        self.ReadCardXML = None
        self.pop = None
        
        self.validaton = [
            self.setIccConfigXML,
            self.UpdateAIDXML,
            self.UpdateKeysXML,
            self.UpdateAIDRulesXML,
            self.pop
            ]
    
    def initializeEMV(self):
        print("Initializing EMV")
        validateRes = self.validateAllReqData()
        
        if validateRes != True:
            print (validateRes)
            return False
        
        pop = self.pop
        
        seticcRes = pop.sendRequest(self.setIccConfigXML)
        
        
    def addPop(self, ip, port):
        '''
        Attach a pop to this emv simulator
        '''
        self.pop = POPCommunicator(ip, port)
    
    def reloadCommandsFromXML(self):
        print("reading commands from xml")
    
    def setSetCommand(self,commandname, commandData):
        '''
        set predefined commands for EMV init and transactions
        '''
        try :
            request = IFSFRequest(commandData)
            if commandname == EMVSimulator.UPDATEAID:
                self.UpdateAIDXML = request
            elif commandname == EMVSimulator.SETICCCONFIG:
                self.setIccConfigXML = request
            elif commandname == EMVSimulator.UPDATEAIDRUEES:
                self.UpdateAIDRulesXML = request
            elif commandname == EMVSimulator.UPDATEKEYS:
                self.UpdateKeysXML = request
            else :
                print ('Invalid Command name provided')
            
        except Exception, e:
            print('Exception while parsing XML',e)
            return False
        
        return True
    
    def validateAllReqData(self):
        for data in self.validaton:
            if data == None :
                return data.getname()
        
        return True