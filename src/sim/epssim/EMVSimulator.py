'''
Created on 01-Feb-2019

@author: VivekK4
'''

from src.sim.epssim.IFSFRequest import IFSFRequest
from src.sim.epssim.POPCommunicator import POPCommunicator
import src.sim.providers.FileDataProvider as FDP
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
    UPDATEAIDRULES = 'UpdateAIDRules'

    def __init__(self, emvCommandProvider = None):
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
        
        if emvCommandProvider is not None:
            self.emvCommandProvider = emvCommandProvider
        else:
            datapro = FDP.FileDataProvider(FDP.FileDataProvider.CONFIG_EMV)
            datapro.initConfig()
            self.emvCommandProvider = datapro
            
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
        
        #TODO: initialize emv and set emv init flag to true
        seticcRes = pop.sendRequest(self.setIccConfigXML)
        
        
    def addPop(self, ip, port):
        '''
        Attach a pop to this emv simulator
        '''
        self.pop = POPCommunicator(ip, port)
    
    def reloadCommandsFromProvider(self):
        print('Reloading commands')
        seticc = self.emvCommandProvider.provideIFSFCommand(EMVSimulator.SETICCCONFIG)
        self.setEMVCommand(EMVSimulator.SETICCCONFIG, seticc)
        
        updateaid = self.emvCommandProvider.provideIFSFCommand(EMVSimulator.UPDATEAID)
        self.setEMVCommand(EMVSimulator.UPDATEAID, updateaid)
        
        updatekeys =  self.emvCommandProvider.provideIFSFCommand(EMVSimulator.UPDATEKEYS)
        self.setEMVCommand(EMVSimulator.UPDATEKEYS, updatekeys)
        
        updateaidrules =  self.emvCommandProvider.provideIFSFCommand(EMVSimulator.UPDATEAIDRULES)
        self.setEMVCommand(EMVSimulator.UPDATEAIDRULES, updateaidrules)
        
        
    def setEMVCommand(self,commandname, commandData):
        '''
        set predefined commands for EMV init and transactions
        '''
    
        request = IFSFRequest(commandData)
        if commandname == EMVSimulator.UPDATEAID:
            self.UpdateAIDXML = request
        elif commandname == EMVSimulator.SETICCCONFIG:
            self.setIccConfigXML = request
        elif commandname == EMVSimulator.UPDATEAIDRULES:
            self.UpdateAIDRulesXML = request
        elif commandname == EMVSimulator.UPDATEKEYS:
            self.UpdateKeysXML = request
        else :
            print ('Invalid Command name provided')
         
        return True
    
    def validateAllReqData(self):
        for data in self.validaton:
            if data == None :
                return data.getname()
        
        return True