from __future__ import print_function
import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from .startup_dialog_ui import Ui_startupDialog
from colorimeter import constants
from colorimeter.gui.basic import startBasicMainWindow
from colorimeter.gui.plot import startPlotMainWindow
from colorimeter.gui.measure import startMeasureMainWindow

class StartupDialog(QtWidgets.QDialog,Ui_startupDialog):

    def __init__(self,parent=None):
        super(StartupDialog,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.initialize()
        self.setAppSize()

    def connectActions(self):
        self.basicPushButton.clicked.connect(
                self.basicPushButtonClicked_Callback
                )
        self.plotPushButton.clicked.connect(
                self.plotPushButtonClicked_Callback
                )
        self.measurePushButton.clicked.connect(
                self.measurePushButtonClicked_Callback
                )

    def reset(self):
        self.program = None

    def initialize(self):
        self.reset()

    def basicPushButtonClicked_Callback(self):
        self.program = startBasicMainWindow
        self.close()

    def plotPushButtonClicked_Callback(self):
        self.program = startPlotMainWindow
        self.close()

    def measurePushButtonClicked_Callback(self):
        self.program = startMeasureMainWindow
        self.close()

    def setAppSize(self):
        availGeom = QtWidgets.QApplication.desktop().availableGeometry()
        x, y = constants.START_POS_X, constants.START_POS_Y
        width = min([0.9*(availGeom.width()-x), self.geometry().width()])
        height = min([0.9*(availGeom.height()-y), self.geometry().height()])
        self.setGeometry(x,y,width,height)

    def run(self):
        self.show()
        self.raise_()
        self.exec_()
        return self.program

def startColorimeterApp():
    app = QtWidgets.QApplication(sys.argv)
    dlg = StartupDialog()
    program = dlg.run()
    while program is not None:
        program(app)
        dlg.reset()
        program = dlg.run()

# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    startColorimeterApp()

