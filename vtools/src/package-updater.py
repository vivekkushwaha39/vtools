import os.path as path
import glob
import os

from color_output import ColorOutput as co

class PackageUpdater :
    
    def __init__( self ):
        
        self.srcPath = "/cygdrive/c/Users/vivekk4/Documents/PackageManagerWorkspaceTwo/*"
        self.destPath = "/cygdrive/c/Users/vivekk4/Documents/PackageManagerWorkspaceOne/*"
    
        self.fileList = []
        self.fileOnlyList = []
        self.fileListDest = []
        self.fileListSrc = []
        
        self.commonFilesIndex = []
        self.newerFileIndex = []
        
    def findAllFiles( self , strPath ):    
        
        fileList = glob.glob( strPath )
                
        for i in fileList :
            
            if ( i == "./" or i == "../" ) :
                print( i + "is current" )
                continue
            
            if path.isdir(i) :
                self.findAllFiles( i + "/*" )
            elif path.isfile(i) and self.isFileRequired( i ) == True :
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
        
        # print "Dest:"
        # print self.fileListDest
        # print "\n"
        
    
    def genSrcFileList( self ):
        self.fileList = []
        self.findAllFiles( self.srcPath )
        self.fileListSrc = self.fileList
        
        # print "Src:"
        # print self.fileListSrc
        # print "\n"
        
    
    def genCommonFiles( self ):
        
        self.fileList = self.fileListSrc
        self.extractFileNames()
        fileListSrc = self.fileOnlyList
        
        self.fileList = self.fileListDest
        self.extractFileNames()
        fileListDest = self.fileOnlyList
        
        indexDest = 0
        indexSrc = 0
        numMatches = 0
        for file1 in fileListDest :
            indexSrc = 0
            numMatches = 0
            
            matchMap = []
            
            for file2 in fileListSrc :
                
                if ( self.compareNames( file1, file2 ) == True ):
                    numMatches += 1
                    
                    # print ( "Files are equal " + self.fileListDest[ indexDest ][63:] + " <=> "  +  self.fileListSrc[ indexSrc ][63:] )
                    # print ( "Files are equal " + file1 + " = "  +  file2 )
                    
                    matchMap.append( { indexDest : indexSrc } )
                    
                indexSrc += 1
            ####################################
            # TODO: remove redundant matches
            ####################################
            if ( numMatches > 0 ) :
                # print ("----------------------------------------------------")
                pass
            
            self.commonFilesIndex =  self.commonFilesIndex + matchMap 
            indexDest += 1
    def compareNames( self , file1 , file2 ):
        if ( file1 == file2 ):
            return True
        else:
            return False
    
    def process( self ):
        
        # remove all p7s and tgz files
        print "Removing p7s Files"
        print os.system( "find " + self.destPath[:-1] + "  -name \"*.p7s\" -delete" )
        print "Removing tgz Files"
        print os.system( "find " + self.destPath[:-1] + " -name \"*.tgz\" -delete" )
        print "Removing tar Files"
        print os.system( "find " + self.destPath[:-1] + " -name \"*.tar\" -delete" )
    
        print "Removing p7s Files"
        print os.system( "find " + self.srcPath[:-1] + "  -name \"*.p7s\" -delete" )
        print "Removing tgz Files"
        print os.system( "find " + self.srcPath[:-1] + " -name \"*.tgz\" -delete" )
        print "Removing tar Files"
        print os.system( "find " + self.srcPath[:-1] + " -name \"*.tar\" -delete" )
    
    
        self.genDestFileList()
        self.genSrcFileList()
        self.genCommonFiles()
        # print ( self.commonFilesIndex )
        self.findNewerFiles()
        print ( self.newerFileIndex )
        
    def printContext( self ) :
        print self.fileList
        
    def isFileRequired( self , fileName ) :
        
        basename = path.basename( fileName )
        
        extension = path.splitext( fileName )[1][1:].lower()
        
        if ( basename == "control" 
            or  basename == "remove" 
            or basename == "Certif.crt" 
            or basename == "SponsorCertif.crt") :
            
            # print "Not required " + fileName
            return False
        # elif ( extension == 'png' 
            # or extension == 'jpg' 
            # or extension == 'jpeg' 
            # or extension == 'wav' 
            # or extension == 'ttf' 
            # or extension == 'frm'
            # or extension == 'tbl'
            # or extension == 'eet' ) :
            
            # # print "not required " + fileName
            # return False
        else :
            return True
    
    
    def findNewerFiles( self ) :
        for entry in self.commonFilesIndex :
            for destIndex, srcIndex in entry.items() :
                
                destFile = self.fileListDest[ destIndex ]
                srcFile = self.fileListSrc[ srcIndex ]
                
                destMTime =   path.getmtime( destFile )
                srcMTime =   path.getmtime( srcFile )
                
                if ( destMTime > srcMTime ) :
                    self.newerFileIndex.append( entry )
                
        for entry in self.newerFileIndex :
            for destIndex, srcIndex in  entry.items() :
                print co.getReset() + "REPLACE " + co.getColorString( co.COLOR_RED ) + self.fileListDest[ destIndex ][63:] \
                + co.getReset()+co.getColorString( co.COLOR_GREEN ) +  " WITH " \
                + co.getReset()+co.getColorString( co.COLOR_RED )  + self.fileListSrc[ srcIndex ][63:]  \
                + co.getReset()
                
                
p = PackageUpdater()
p.process()