# Seperate gui logic vs App logic
# Etsi wste an thelw na allaksw kati sto gui na mhn ephreastei to app logic
# An peiraksw to gui me to designer to gui.py tha allaksei kai oles oi allages tha xathoun 
# Gi auto ftiaxnw neo script
import featuretools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from io import StringIO
from guiv1 import Ui_MainWindow
from functions import Func
import sys, csv
import pandas as pd
import sklearn
import os
class MainWindowUIClass( Ui_MainWindow ):
    def __init__(self):
        global t_left
        super().__init__()
        self.functions = Func()
        

    def setupUi( self, MW ):
        super().setupUi( MW )

    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # --------------------- PRWTO SCREEN ME IMPORT ------------------------
    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    def refreshAll( self ):
        self.pathLine.setText( self.functions.getFileName() )
    
    def browseSlot( self ):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "CSV Files (*.csv)",
                        options=options)
        if fileName:
            self.functions.setFileName( fileName )
            self.refreshAll()

    def importSlot( self ): # Slot gia to import button
        global fileName
        fileName = self.pathLine.text()
        if self.functions.isValid( fileName ):
            global data
            data = self.functions.readFile(fileName)
            self.functions.setFileName( self.pathLine.text() )
            self.refreshAll()
            m = QtWidgets.QMessageBox()
            m.setText("File was successfully imported!")
            m.setStandardButtons(QtWidgets.QMessageBox.Ok)
            m.setDefaultButton(QtWidgets.QMessageBox.Ok)
            ret = m.exec_()
            self.refreshAll()
            self.nextButton.setEnabled(True) # Otan ginei to import me valid file energopoieitai to next button
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Choose a valid file to import!")
            m.setStandardButtons(QtWidgets.QMessageBox.Ok)
            m.setDefaultButton(QtWidgets.QMessageBox.Ok)
            ret = m.exec_()
            self.refreshAll()
            
    def cancelSlot(self): # Slot gia to cancel button --> KANONIKA KANEI CLEAR ALLA TO EXW ETSI GIA EUKOLIA
        self.pathLine.setText("/home/ggeorg/Desktop/DataSets/iris.csv") 

    def nextSlot( self ): # Slot gia to next button
        self.stackedWidget.setCurrentIndex(1)
        # Molis pataw next tha kanei load to combo Box kai tha periexei ta features.
        # iterating the columns 
        for col in data.columns: 
            self.comboBox.addItem(col) 
        #dimiourgia table me ta dedomena tou dataset gia preview
        self.tableWidget.setRowCount(20) # set row Count
        self.tableWidget.setColumnCount(self.functions.colCount(data)) # set column count
        for i in range(20):
            for j in range(self.functions.colCount(data)):
                self.tableWidget.setItem(i,j, QTableWidgetItem( f"{ data.iloc[i][j] }" ))
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # --------------------- SCREEN ME TARGET KAI PREDICTOR FEATURES -------
    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    def featureSlot( self ): # Slot gia to drop down box
        item_index = self.comboBox.currentIndex()
        print(f"Ok. Column {item_index} is your Target Feature! ")
        global X
        global y
        y = self.functions.pickTarget(item_index, data)
        X = self.functions.pickPredictors(item_index, data)
        self.nextButton1.setEnabled(True) # Otan ginei to import me valid file energopoieitai to next button
        for i in range(20):
            for j in range(self.functions.colCount(data)):
                self.tableWidget.item(i,j).setBackground(QtGui.QColor('white'))
            self.tableWidget.item(i,item_index).setBackground(QtGui.QColor('springgreen'))

    def backSlot( self ): # Slot gia to back button
        self.stackedWidget.setCurrentIndex(0) # Pame ena screen pisw
        self.comboBox.clear() # Katharizoyme to Combo box gia na mpoun nea features sto drop down
        self.nextButton.setEnabled(False) # Otan ginei to import me valid file energopoieitai to next button

    def nextSlot_1(self): # Next pou pigainei stis parametrous tou modeling
        self.stackedWidget.setCurrentIndex(2) # Pame ena screen mprosta sto next screen me preprocessing / modeling k parameter tuning        
        global  inc_est, exc_est, inc_pre, exc_pre, resample, resample_args, metric, disable_prepro

        #MODELING DEFAULTS        
        self.timeLeft_box.setMinimum(30) 
        self.timeLeft_box.setMaximum(30000) 

        self.perRun_box.setMinimum(3)
        self.perRun_box.setMaximum(int(t_left/2))

        meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())# analoga me ta specs tou pc
        mem_Mb = int(meminfo['MemTotal']/1024)  
        self.memory_box.setMinimum(1024)
        self.memory_box.setMaximum(mem_Mb) 

        metric_list = ["accuracy", "balanced_accuracy", "roc_auc", "average_precision", "log_loss",
        "precision", "precision_macro", "precision_micro", "precision_samples", "precision_weighted",
        "recall","recall_macro","recall_micro","recall_samples","recall_weighted",
        "f1", "f1_macro", "f1_micro", "f1_samples", "f1_weighted"]
        self.metricCombo.addItems(metric_list)
        metric = None
        resample_args = None
        resample_list = ["None", "Cross Validation", "Holdout"]
        self.ressampleCombo.addItems(resample_list)
        resample = 'holdout'
        inc_est = None
        exc_est = None

    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><><
    # --------------------- MODELING SCREEN -------------------------------
    # ><><><><><<><><><><><><><><><><><<><><><><><><><><><><><<><><><><><>< 
    # Time Left For This Task 
    def timeleft_Slot(self):
        global t_left
        t_left = self.timeLeft_box.value()
        self.perRun_box.setMaximum(int(t_left/2))
        print (t_left)

    # Per Run Time Limit
    def perrun_Slot(self): 
        global t_per_run
        t_per_run = self.perRun_box.value()
        print (t_per_run)

    # Ensemble Memory Limit
    def ensmemory_Slot(self):
        global mem_limit
        mem_limit = self.memory_box.value()

    # Metric
    def metricBox(self):
        combo_idx_metric = self.metricCombo.currentIndex()
        metric = self.metricCombo.itemText(combo_idx_metric)

    # Resample
    def resampleBox(self):
        combo_idx_resample = self.ressampleCombo.currentIndex()
        resample_str = self.ressampleCombo.itemText(combo_idx_resample)
        if resample_str == "Cross Validation":
            resample = 'cv'
        elif resample_str == "None":
            resample = None
        else:
            resample = 'holdout'
    
    # Go !
    
    def nextSlot_2(self):
        pass
    def backSlot_1(self):
        pass

    def adaChecked(self):
        print("ada checked")

    def prepro_Checked(self): # Disable Feature Preprocessing
        global disable_prepro
        if self.checkBox_16.isChecked():    
            disable_prepro = ["no_preprocessing"]
        else:
            disable_prepro = None
                
    def modelSlot(self):
        print("please wait... May take several seconds...")
        X_train, X_test, y_train, y_test = self.functions.splitData(X, y)
        base = os.path.basename(fileName)
        dataset_name = os.path.splitext(base)[0]
        global model
        model = self.functions.callClassifier(t_left, t_per_run, mem_limit, inc_est, exc_est, disable_prepro, resample, resample_args, metric)
        self.functions.fitModel(X_train, y_train, model, dataset_name)
        print (model.sprint_statistics())
        
        pred = model.predict(X_test)
        print("Accuracy score", sklearn.metrics.accuracy_score(y_test, pred))
        print(model.show_models())
# Main         
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindowUIClass()
    MainWindow = QtWidgets.QMainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()