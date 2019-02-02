'''
Created on 02-Feb-2019

@author: vivek_
'''

from src.utils.InputUtils import readmultiline
from src.sim.epssim.IFSFRequest import IFSFRequest
from src.sim.epssim.IFSFRequestEditor import IFSFRequestEditor
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
    editor.printXML()
    a="""
    asdsad
    asdsad
    asdsa"""
    print(a)

editorTest()