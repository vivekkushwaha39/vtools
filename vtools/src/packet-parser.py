import sys





packetFormat = {

	'meta' : {
		'humanName' : 'Request APDU Format'
	},

	'format' :[
		{
			'humanName' : 'CLA',
			'len' : 2,
			'lenType' : 'char'
		},
		{
			'humanName' : 'INS',
			'len' : 2,
			'lenType' : 'char'
		},
		{
			'humanName' : 'PLA',
			'len' : 2,
			'lenType' : 'char'
		}
	]
	
}

packetData = 'AABBb';

class PacketParser:
	
	def __init__(self , packetFormat , packetData):
		
		self.packetFormat = packetFormat
		self.packetData = packetData
		self.process()
		
		pass
		
	def process(self):
		
		data = self.packetData
		format = self.packetFormat['format']
		
		for i in range(len(format))  :
			currPack = format[i]
			if ( len(data) < currPack['len'] ):
				print (" Not enough data to parse " )
				print ('Data len for ' + currPack['humanName'] + ' is ' + str(currPack['len']) + ' unit but found only ' + str(len(data) ) + ' unit' )
				exit()
			
			curInString = data[0:currPack['len'] ]
			data = data[ currPack['len'] :]
			print ( currPack['humanName'] +' = ' + curInString )
	

	
parser = PacketParser(packetFormat, packetData)