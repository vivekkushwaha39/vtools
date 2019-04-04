'''
Created on 03-Feb-2019

@author: vivek_
'''
import tkinter as tk
from tkinter.ttk import *  # @UnusedWildImport
# from Tkconstants import *  # @UnusedWildImport
from tkinter.constants import *
from vtools.src.sim.epssim import CommandParserLeg
from vtools.src.sim.epssim.POPCommunicator import POPCommunicator


class EPSUILeg:
    
    def __init__(self):
        self.pop = None
        self.pop = POPCommunicator('192.168.31.127', 4000)
    
    def runUI(self):
        commandParser = CommandParserLeg.CmdParserLeg()
        
        root = tk.Tk()
        root.title("EPS Simulator")
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        # main frame which will hold all controls
        mainFrame = tk.Frame(root)
        mainFrame.grid(column=0, row=0, sticky=E+W+N+S)
        mainFrame.rowconfigure(0, weight=1)
        mainFrame.columnconfigure(0, weight=1)
        
        # frame for commands
        frmCommands = tk.Frame(mainFrame)
        frmCommands.grid(column=0, row=0, sticky=(E, W))
        
        # frame for logs
        frmLog = tk.Frame(mainFrame, bg="red")
        frmLog.grid(column=0, row=1, sticky=(E, W, N, S))
    
        self.txtLog  = tk.Text(frmLog)
        self.txtLog.grid(row=0, column=0, sticky=(W, N, S))
        
        lblConnStatus = Label(frmLog,text='Ready')
        lblConnStatus.grid(row=0, column=1)
        
        btnCommands = []
        
        '''
            Commands which are present in file
        '''
        self.commands = commandParser.getCommands()
        
        count = 0
        maxCol = 5
        for cmd in self.commands :
            btn = Button(frmCommands, text=cmd, width=30,
                          command=lambda name=cmd+'': self.btnSendCommand_Click(name))
            row = count / maxCol
            col = count % maxCol
#             print('Row is {0} col {1}'.format(row, col))
            btn.grid(row=int(row), column=col)
            btnCommands.append(btn)
            count = count +1
        
        # Set resize properties here
        EPSUILeg.configColumns(frmCommands, 1)
        EPSUILeg.configRows(frmCommands, 1)
        
        EPSUILeg.configColumns(frmLog, 1)
        EPSUILeg.configRows(frmLog, 1)
        
        # program main loop
        root.mainloop()
    
    @staticmethod
    def configRows(ctrl, weight):
        row, col = ctrl.grid_size()
        for i in range(row):
            ctrl.rowconfigure(i, weight=weight)
    @staticmethod
    def configColumns(ctrl, weight):
        row, col = ctrl.grid_size()
        for i in range(col):
            ctrl.columnconfigure(i, weight=weight)
        
    def btnSendCommand_Click(self, commandName):
        requestCommand = self.commands[commandName]
        cmdString = requestCommand.genXMLString()
        self.txtLog.insert(END, cmdString)
        self.pop.sendRequest(cmdString)
		
        