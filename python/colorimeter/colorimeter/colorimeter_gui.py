import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from colorimeter_gui_ui import Ui_MainWindow 
from colorimeter import Colorimeter

DFLT_PORT = '/dev/ttyUSB2'


class ColorimeterMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(ColorimeterMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.initialize()

    def connectActions(self):
        self.portLineEdit.editingFinished.connect(self.portChanged_Callback)
        self.connectPushButton.pressed.connect(self.connectPressed_Callback)
        self.connectPushButton.clicked.connect(self.connectClicked_Callback)
        self.calibratePushButton.clicked.connect(self.calibrateClicked_Callback)
        self.measurePushButton.clicked.connect(self.measureClicked_Callback)

    def initialize(self):
        self.port = DFLT_PORT
        self.portLineEdit.setText(self.port) 
        self.setWidgetEnableOnDisconnect()
        self.dev = None

    def portChanged_Callback(self):
        self.port = str(self.portLineEdit.text())

    def connectPressed_Callback(self):
        if self.dev == None:
            self.connectPushButton.setText('Disconnect')
            self.portLineEdit.setEnabled(False)

    def connectClicked_Callback(self):
        if self.dev == None:
            self.dev = Colorimeter(self.port)
            self.setWidgetEnableOnConnect()
        else:
            self.connectPushButton.setText('Connect')
            self.dev.close()
            self.dev = None
            self.setWidgetEnableOnDisconnect()

    def calibrateClicked_Callback(self):
        self.dev.calibrate()

    def measureClicked_Callback(self):
        freq, trans, absorb = self.dev.getMeasurement()
        transStrList = [
                'red:    {0:1.2f}'.format(trans[0]),
                'green:  {0:1.2f}'.format(trans[1]),
                'blue:   {0:1.2f}'.format(trans[2]),
                'white:  {0:1.2f}'.format(trans[3]),
                ]
        transStr = '\n'.join(transStrList)
        self.transmissionTextEdit.setText(transStr)
                
        absorbStrList = [ 
                'red:    {0:1.2f}'.format(absorb[0]),
                'green:  {0:1.2f}'.format(absorb[1]),
                'blue:   {0:1.2f}'.format(absorb[2]),
                'white:  {0:1.2f}'.format(absorb[3]),
                ]
        absorbStr = '\n'.join(absorbStrList)
        self.absorbanceTextEdit.setText(absorbStr)

    def setWidgetEnableOnConnect(self):
        self.transmissionTextEdit.setEnabled(True)
        self.absorbanceTextEdit.setEnabled(True)
        self.calibratePushButton.setEnabled(True)
        self.measurePushButton.setEnabled(True)
        self.portLineEdit.setEnabled(False)

    def setWidgetEnableOnDisconnect(self):
        self.transmissionTextEdit.setEnabled(False)
        self.absorbanceTextEdit.setEnabled(False)
        self.calibratePushButton.setEnabled(False)
        self.measurePushButton.setEnabled(False)
        self.portLineEdit.setEnabled(True)

    def main(self):
        self.show()

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mainWindow = ColorimeterMainWindow()
    mainWindow.main()
    app.exec_()