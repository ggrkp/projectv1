# Seperate gui logic vs App logic
# Etsi wste an thelw na allaksw kati sto gui na mhn ephreastei to app logic
# An peiraksw to gui me to designer to gui.py tha allaksei kai oles oi allages tha xathoun 
# Gi auto ftiaxnw neo script

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from guiv1 import Ui_MainWindow 
from model import Model

import sys

class MainWindowUIClass( Ui_MainWindow ):
    def __init__(self):
        super().__init__()
        self.model = Model()
    def setupUi( self, MW ):
        super().setupUi( MW )


    def refreshAll( self ):
        self.pathLine.setText( self.model.getFileName() )

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
            self.model.setFileName( fileName )
            self.refreshAll()

    def importSlot( self ): # Slot gia to import button
        fileName =  self.pathLine.text()
        if self.model.isValid( fileName ):
            self.model.setFileName( self.pathLine.text() )
            self.refreshAll()
            m = QtWidgets.QMessageBox()
            m.setText("File was successfully imported!")
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                    | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Ok)
            ret = m.exec_()
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Choose a valid file to import!")
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                    | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Ok)
            ret = m.exec_()
            self.refreshAll()

    def cancelSlot(self): # Slot gia to cancel button
        self.pathLine.setText("") 

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()