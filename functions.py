# Edw tha uparxei to file pou tha ginei load kai ta periexomena tou 
# ola tha emfanizontai sto GUI (logika)
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from guiv1 import Ui_MainWindow
from sklearn.model_selection import train_test_split
from autosklearn.classification import AutoSklearnClassifier
import sklearn 
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
        target = df.iloc[:, (tar_idx)].to_numpy()  # Target Variable
        return target
        
    def pickPredictors(self, tar_idx, df):
        predictors = df.iloc[:, df.columns != df.columns[tar_idx]].to_numpy()  # Predictor Variables (All except the Target one.)              
        return predictors        
    
    def rowCount(self, df):
        return df.shape[0]

    def colCount(self, df):
        return df.shape[1]
    
    def hasHeader(self, df):
        pass
    
    # nees sunartiseis 

    def splitData(self, pred, target):
        return train_test_split( pred, target, test_size = 0.2, random_state=1 )

    def callClassifier(self, t_left, t_per_run, mem_limit, inc_est, disable_prepro, resample, resample_args, metric):
        automl = AutoSklearnClassifier(
        # TIME RESTRICTION
        time_left_for_this_task=t_left,
        per_run_time_limit=t_per_run,

        #MEMORY RESTRICTION
        ensemble_memory_limit= mem_limit, 

        #ALGORITHM RESTRICTION
        include_estimators= inc_est,

        #APENERGOPOIHSH PREPROSSESORS
        include_preprocessors= disable_prepro,

        #RESAMPLING (CROSS VALIDATION) - ISWS ME NEA SUNARTHSH GIA NA PAIRNEI KI AUTO PARAMETROUS
        resampling_strategy=resample, 
        resampling_strategy_arguments= resample_args,
        #EPILOGI METRIKWN
        metric= metric 
        )
        return automl
    
    def callRegressor(self):
        automl = AutoSklearnClassifier(
        time_left_for_this_task=30,
        )
        return automl

    #isws sinartisi na epilegei classifier i regressor meta
    def fitModel(self, pred_train, target_train, automl, d_name):
        automl.fit(pred_train, target_train, dataset_name = d_name)

    def app_Estimator(self, inc_est, box_state, est_name ):
        if box_state:
            if not est_name in inc_est:
                inc_est.append(est_name)
        else:
            if est_name in inc_est:
                inc_est.remove(est_name)
        return(inc_est)
    # def getScore(self, automl, p_test, t_test):
    #     pred = automl.predict(p_test)
    #     return sklearn.metrics.accuracy_score(t_test, pred)




 

        