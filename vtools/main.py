'''
Created on 02-Feb-2019

@author: vivek_
'''
from vtools.src.utils.InputUtils import readmultiline
from vtools.src.sim.epssim.IFSFRequest import IFSFRequest
from vtools.src.sim.epssim.IFSFRequestEditor import IFSFRequestEditor
import vtools.src.sim.epssim.EMVSimulator as ES
import os
def inputTest():
    print('Enter XML now')
    xmlData = readmultiline()
    print('Data is',xmlData)
    req = IFSFRequest(xmlData)
    req.parse()
    req.selectInsecureDataByIndex(0)
    print (req.getValFromCurrInsecData('9F02'))

def editorTest():
    print('Enter XML now')
    xmlData = readmultiline()
    req = IFSFRequest(xmlData)
    req.parse()
    editor = IFSFRequestEditor(req)
    editor.editInNpp()
    raw_input('Press enter when done')
    editor.refreshFromEditedFile()


def simTest():
    print('Testing simulator')
    sim = ES.EMVSimulator()
    sim.reloadCommandsFromProvider()
    
def editorTest2():
    print('Enter XML now')
    xmlData = readmultiline()
    req = IFSFRequest(xmlData)
    req.parse()
    editor = IFSFRequestEditor(req)
    editor.editForAID('A00000023232')

    
os.chdir('../../')
editorTest2()
