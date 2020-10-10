# Edw tha uparxei to file pou tha ginei load kai ta periexomena tou 
# ola tha emfanizontai sto GUI (logika)
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from guiv1 import Ui_MainWindow

import sys, csv
import featuretools as ft
class Func:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None

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
        target = df.iloc[:, (tar_idx)]  # Target Variable
        return target
        
    def pickPredictors(self, tar_idx, df):
        predictors = df.iloc[:, df.columns != df.columns[tar_idx]]  # Predictor Variables (All except the Target one.)              
        return predictors        
    
    def rowCount(self, df):
        return df.shape[0]

    def colCount(self, df):
        return df.shape[1]
    
    def featureSunthesis(self, predictors): 
        pass

    def testtrainSplit(self, df):
        pass

    def preprocessData(self, df):
        pass

    def hasHeader(self, df):
        pass

        