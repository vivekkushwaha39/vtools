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
            'humanName': 'E0 template',
            'len' : -1,
            'lenType' : 'char'
        },
        {
            'humanName' : 'PLA',
            'len' : 2,
            'lenType' : 'char'
        }
    ]
    
}

definedTags = [
    'dfdf30',
    'dff01'
]


packetData = 'dfdf30010Adff0102ffff';

class PacketParser:
    
    def __init__(self , packetFormat , packetData):
        
        # self.packetFormat = packetFormat
        # self.packetData = packetData
        # self.process()
        self.parseTemplates( packetData )
        pass
        
    def process(self):
        
        data = self.packetData
        format = self.packetFormat['format']
        
        for i in range(len(format))  :
            currPack = format[i]
            
            curInString = data[0:currPack['len'] ]
            data = data[ currPack['len'] :]
            print ( currPack['humanName'] +' = ' + curInString )
    
    def parseTemplates(self, templateData):
        retbool = True
        currIndex = 0
        
        while( currIndex < len(templateData) ):
            firstTag = self.getFirstTag( templateData[currIndex:] )
            if ( firstTag != '' ):
                firstTagLen = len(firstTag)
                strValueLen = templateData[ currIndex + firstTagLen : currIndex + firstTagLen + 2 ]
                valueLen = int(strValueLen, 16) * 2 # * by 2 beacuse we need to skip 2 chars for 1 byte of data
                strValue = templateData[ currIndex + firstTagLen + 2 : currIndex + firstTagLen + 2 + valueLen ]
                self.printTagValMeaning(firstTag, strValue)                
                currIndex = currIndex + firstTagLen + 2 + valueLen
                pass
            else:
                retbool = False
                break
        return retbool
    def printTagValMeaning(self, tag, val):
        print ( 'Found tag', tag,' Val', val )
        pass
    
    def getFirstTag(self, strData ):
        retTag = ''
        for index in range(len(definedTags)) :
            tag = definedTags[index]
            taglen = len(tag)
            if ( tag == strData[0:taglen] ):
                retTag = strData[0:taglen]
                break
        return retTag

parser = PacketParser(packetFormat, packetData)