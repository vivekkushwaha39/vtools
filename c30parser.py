import sys
class C30Util:
	def __init__(self):
		print( sys.argv[2])
		self.str = sys.argv[2]


	def doWork(self):
		i = 0
		insideCone = False
		totalStr = ''
		while(i < len(self.str) ):
			printStr = ''
			if ( self.str[i] == '<' ):
				# printStr = '<'
				insideCone = True
			elif ( self.str[i] == '>' ):
				# printStr = '>'
				insideCone = False
			elif ( insideCone == False ) :
				printStr = `ord(self.str[i])`
			else :
				printStr = self.str[i]
			totalStr += printStr
			i = i+1
	
		print(totalStr)