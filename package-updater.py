import os.path as path
import glob

class PackageUpdater :
    
    def __init__( self ):
        
        self.srcPath = "./test1/*"
        self.destPath = "./test2/*"
    
        self.fileList = []
        self.fileOnlyList = []
        self.fileListDest = []
        self.fileListSrc = []
        self.commonFilesIndex = []
    
    def findAllFiles( self , strPath ):    
        
        fileList = glob.glob( strPath )
                
        for i in fileList :
            
            if ( i == "./" or i == "../" ) :
                print( i + "is current" )
                continue
            
            if path.isdir(i) :
                self.findAllFiles( i + "/*" )
            elif path.isfile(i) :
                self.fileList.append(i);
    
    
    def printFileList( self ):
        self.extractFileNames()
        print ( self.fileList )
        print ( "\n" )
        print ( self.fileOnlyList )
    
    def extractFileNames( self ):
        self.fileOnlyList = []
        for file in self.fileList :
            currFile = path.basename( file )
            self.fileOnlyList.append( currFile )
    
    def genDestFileList( self ):
        self.fileList = []
        self.findAllFiles( self.destPath )
        self.fileListDest = self.fileList
        
    
    def genSrcFileList( self ):
        self.fileList = []
        self.findAllFiles( self.srcPath )
        self.fileListSrc = self.fileList
    
    def genCommonFiles( self ):
        
        self.fileList = self.fileListSrc
        self.extractFileNames()
        fileListSrc = self.fileOnlyList
        
        self.fileList = self.fileListDest
        self.extractFileNames()
        fileListDest = self.fileOnlyList
        
        print "Src:"
        print self.fileListSrc
        print "\n"
        
        print "dest:"
        print self.fileListDest
        print "\n"
        
        indexDest = 0
        indexSrc = 0
        
        for file1 in fileListDest :
            indexDest += 1
            indexSrc = 0 
            for file2 in fileListSrc :
                indexSrc += 1
                if ( self.compareNames( file1, file2 ) == True ):
                    print ( "Files are equal " + file1 + "=" + file2 )
                    self.commonFilesIndex.append( { indexDest : indexSrc } )
                    
    def compareNames( self , file1 , file2 ):
        if ( file1 == file2 ):
            return True
        else:
            return False
    
    def process( self ):
        self.genDestFileList()
        self.genSrcFileList()
        self.genCommonFiles()
        print ( self.commonFilesIndex )
        
    def printContext( self ) :
        print self.fileList
    
p = PackageUpdater()
p.process()