import sys
class AsciiUtil:
	def __init__(self):
		print( sys.argv[3])
		self.str = sys.argv[3]


	def doWork(self):
		i = 0
		while(i < len(self.str) ):
			nStr = self.str[ i : i+2]
			num = int(nStr , 16)
			print( nStr, ' => ',   chr(num))
			i += 2

