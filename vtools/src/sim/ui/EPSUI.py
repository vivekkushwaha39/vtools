'''
Created on 03-Feb-2019

@author: vivek_
'''
from tkinter import *
from tkinter.ttk import *

def runUI():
    root = Tk()
    
    frmCommands = Frame(root)
    frmCommands.grid(row=0,column=0)
    
    btnCommands = []
    
    numCol=3
    for i  in range(10):
        btn = Button(frmCommands, text="Button "+str(i+1))
        row = int(i)/int(numCol)
        col = i % numCol
        print('Row is {0} col {1}'.format(row, col))
        
        btn.grid(row=row, column=col, stickey=S,master=frmCommands)
       
        btnCommands.append(btn)
    
        
    root.mainloop()
