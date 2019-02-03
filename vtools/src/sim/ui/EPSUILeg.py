'''
Created on 03-Feb-2019

@author: vivek_
'''
from Tkinter import Tk, Text
from ttk import *
from Tkconstants import *
from vtools.src.sim.epssim import CommandParserLeg


def runUI():
    commandParser = CommandParserLeg.CmdParserLeg()
    
    root = Tk()
    
    frmCommands = Frame(root)
    frmCommands.pack(fill=BOTH, side=LEFT)
    
#     rows = 0
#     while rows < 50:
#         frmCommands.rowconfigure(rows, weight=1)
#         frmCommands.columnconfigure(rows,weight=1)
#         rows += 1
     
    frmLog = Frame(root)
    frmLog.pack(fill=BOTH, side=RIGHT)
    
    txtLog = Text(frmLog,height=20)
    txtLog.grid(row=0, column=0)
    
    lblConnStatus = Label(frmLog,text='Ready')
    lblConnStatus.grid(row=1, column=0)
    
    btnCommands = []
    commands = commandParser.getCommands()
    count = 0
    maxCol = 3
    for cmd in commands :
        btn = Button(frmCommands, text=cmd, width=30,
                      command=lambda name=cmd+'': btnSendCommand_Click(name))
        row = count / maxCol
        col = count % maxCol
        print('Row is {0} col {1}'.format(row, col))
        btn.grid(row=row, column=col)
        btnCommands.append(btn)
        count = count +1
    
    root.mainloop()

def btnSendCommand_Click(evt):
    
    print evt
