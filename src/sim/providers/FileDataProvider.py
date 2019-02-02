'''
Created on 02-Feb-2019

@author: vivek_
'''
import src
import os
class FileDataProvider:
    '''
    Data provider from file
    '''
    CONFIG_EMV = 0
    
    def __init__(self, configType):
        '''
        Constructor
        '''
        self.config = configType
        self.fileDict = {}
        
    def initConfig(self):
       
        if self.config == FileDataProvider.CONFIG_EMV :
            self.fileDict[src.sim.epssim.EMVSimulator.EMVSimulator.SETICCCONFIG] = 'res/SetICCConfig.xml'
            self.fileDict[src.sim.epssim.EMVSimulator.EMVSimulator.UPDATEAID] = 'res/UpdateAID.xml'
            self.fileDict[src.sim.epssim.EMVSimulator.EMVSimulator.UPDATEKEYS] = 'res/UpdateKeys.xml'
            self.fileDict[src.sim.epssim.EMVSimulator.EMVSimulator.UPDATEAIDRULES] = 'res/UpdateAIDRules.xml'
            
    def provideIFSFCommand(self, commandName):
        os.system('pwd')
        print('Providing command from ', self.fileDict[commandName])
        commandFile = open(self.fileDict[commandName], 'r')
        content = commandFile.read()
        commandFile.close()
        return content   
