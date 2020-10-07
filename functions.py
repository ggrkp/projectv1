# Edw tha uparxei to file pou tha ginei load kai ta periexomena tou 
# ola tha emfanizontai sto GUI (logika)
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from guiv1 import Ui_MainWindow
import sys, csv
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
        else:
            self.fileName = ""
            
    def getFileName( self ):
        return self.fileName
    
    def readFile(self, fileName):
        df = pd.read_csv(fileName, sep="[,;]", engine='python') # Read DataFrame     
        return df

    def pickTarget(self, tar_idx , df):
        y = df.iloc[:, (tar_idx)]  # Target Variable
        return y
        
    def pickPredictors(self, tar_idx, df):
        X = df.iloc[:, df.columns != df.columns[tar_idx]]  # Predictor Variables (All except the Target one.)              
        return X

    def showCSV(self):
        pass
    
    def createFeature(self):
        pass
    
    
