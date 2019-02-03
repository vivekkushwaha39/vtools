#python
import sys
from asciiparser import AsciiUtil
from c30parser import C30Util
commandList = {
	'ascii' : AsciiUtil,
	'c30' : C30Util
}

if ( len(sys.argv) <= 2 ):
	print( 'Inavlid no of args' )
	exit()
	
className = commandList[sys.argv[1]]

executerObject = className()
executerObject.doWork()