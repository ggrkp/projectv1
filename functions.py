# Edw tha uparxei to file pou tha ginei load kai ta periexomena tou 
# ola tha emfanizontai sto GUI (logika)
import pandas as pd

class Func:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None
        self.fileContent = ""

    def isValid( self, fileName ): # checks if file exists
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        if self.isValid( fileName ):
            self.fileName = fileName
            self.fileContents = open( fileName, 'r' ).read()
        else:
            self.fileContents = ""
            self.fileName = ""
            
    def getFileName( self ):
        return self.fileName
    
    def readFile(self, fileName):
        df = pd.read_csv(fileName, sep="[,;]", engine='python',  skiprows=1, header=None) # Read DataFrame     
        print(df.head())
        return df

    def showCSV(self):
        pass
    
    def createFeature(self):
        pass
    
   
