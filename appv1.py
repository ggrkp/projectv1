# Seperate gui logic vs App logic
# Etsi wste an thelw na allaksw kati sto gui na mhn ephreastei to app logic
# An peiraksw to gui me to designer to gui.py tha allaksei kai oles oi allages tha xathoun 
# Gi auto ftiaxnw neo script
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from guiv1 import Ui_MainWindow
from functions import Func
import sys, csv
import pandas as pd
class MainWindowUIClass( Ui_MainWindow ):
    def __init__(self):
        super().__init__()
        self.functions = Func()
    def setupUi( self, MW ):
        super().setupUi( MW )


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
        fileName =  self.pathLine.text()
        if self.functions.isValid( fileName ):
            x = self.functions.readFile(fileName)
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

    def cancelSlot(self): # Slot gia to cancel button
        self.pathLine.setText("/home/ggeorg/Desktop/DataSets/iris.csv") 

    def nextSlot( self ): # Slot gia to next button
        self.stackedWidget.setCurrentIndex(1)
        # Molis pataw next tha kanei load to combo Box kai tha periexei ta features.
        fileName = self.functions.getFileName()
        data = self.functions.readFile(fileName)
        # iterating the columns 
        for col in data.columns: 
            self.comboBox.addItem(col) 

    def backSlot( self ): # Slot gia to back button
        self.stackedWidget.setCurrentIndex(0) # Pame ena screen pisw
        self.comboBox.clear() # Katharizoyme to Combo box gia na mpoun nea features sto drop down

    def featureSlot( self ): # Slot gia to drop down box
        item_index = self.comboBox.currentIndex()
        print(f"Ok. Column {item_index} is your Target Feature! ")
        fileName = self.functions.getFileName()
        df = self.functions.readFile(fileName)
        y = self.functions.pickTarget(item_index, df)
        X = self.functions.pickPredictors(item_index, df)
            

    # MAIN
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindowUIClass()
    MainWindow = QtWidgets.QMainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()