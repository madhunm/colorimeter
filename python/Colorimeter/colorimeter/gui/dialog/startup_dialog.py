from __future__ import print_function
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from startup_dialog_ui import Ui_startupDialog
from colorimeter import constants
from colorimeter.gui.basic import startBasicGUI
from colorimeter.gui.plot import startPlotGUI
from colorimeter.gui.measure import startMeasureGUI

class StartupDialog(QtGui.QDialog,Ui_startupDialog):

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

    def initialize(self):
        self.program = None

    def basicPushButtonClicked_Callback(self):
        self.program = startBasicGUI
        self.close()

    def plotPushButtonClicked_Callback(self):
        self.program = startPlotGUI
        self.close()

    def measurePushButtonClicked_Callback(self):
        self.program = startMeasureGUI
        self.close()

    def setAppSize(self):
        availGeom = QtGui.QApplication.desktop().availableGeometry()
        x, y = constants.START_POS_X, constants.START_POS_Y
        width = min([0.9*(availGeom.width()-x), self.geometry().width()])
        height = min([0.9*(availGeom.height()-y), self.geometry().height()])
        self.setGeometry(x,y,width,height)

    def run(self):
        self.show()
        self.exec_()
        return self.program

# ---------------------------------------------------------------------------------
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    dlg = StartupDialog()
    program = dlg.run()
    if program is not None:
        program()
