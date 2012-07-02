from __future__ import print_function
import os, sys, platform
import functools
import random, re, time
import matplotlib
matplotlib.use('Qt4Agg')
from matplotlib import pylab

from PyQt4 import QtCore
from PyQt4 import QtGui

from colorimeter_measurement_ui import Ui_MainWindow 
from colorimeter_serial import Colorimeter

DFLT_PORT_WINDOWS = 'com1' 
DFLT_PORT_LINUX = '/dev/ttyACM0' 
MIN_ROW_COUNT = 5
COL_COUNT = 2

class MeasurementMainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self,parent=None):
        super(MeasurementMainWindow,self).__init__(parent)
        self.radioButtonColors = ('red', 'green', 'blue', 'white')
        self.setupUi(self)
        self.connectActions()
        self.initialize()

    def connectActions(self):
        self.portLineEdit.editingFinished.connect(self.portChanged_Callback)
        self.connectPushButton.pressed.connect(self.connectPressed_Callback)
        self.connectPushButton.clicked.connect(self.connectClicked_Callback)
        self.measurePushButton.clicked.connect(self.measureClicked_Callback)
        self.measurePushButton.pressed.connect(self.measurePressed_Callback)
        self.clearPushButton.pressed.connect(self.clearPressed_Callback)
        self.clearPushButton.clicked.connect(self.clearClicked_Callback)

        for color in self.radioButtonColors:
            button = getattr(self,'{0}RadioButton'.format(color))
            callback = functools.partial(self.colorRadioButton_Clicked, color)
            button.clicked.connect(callback)
        self.plotPushButton.clicked.connect(self.plotPushButton_Clicked)

    def initialize(self):
        osType = platform.system()
        if osType == 'Linux': 
            self.port = DFLT_PORT_LINUX 
        else: 
            self.port = DFLT_PORT_WINDOWS 
        self.userHome = os.getenv('USERPROFILE')
        if self.userHome is None:
            self.userHome = os.getenv('HOME')
        self.lastLogDir = self.userHome
            
        self.portLineEdit.setText(self.port) 
        self.measIndex = 0
        self.dev = None
        self.redRadioButton.setChecked(True)
        self.currentColor_str = 'red'
        self.statusbar.showMessage('Not Connected')

        pylab.ion()

        # Set up data table
        self.cleanDataTable(setup=True)
        self.setWidgetEnabledOnDisconnect()

        self.tableWidget.setHorizontalHeaderLabels(('Concentration','Absorbance')) 
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def portChanged_Callback(self):
        self.port = str(self.portLineEdit.text())

    def connectPressed_Callback(self):
        if self.dev == None:
            self.connectPushButton.setText('Disconnect')
            self.connectPushButton.setFlat(True)
            self.portLineEdit.setEnabled(False)
            self.statusbar.showMessage('Connecting...')

    def connectClicked_Callback(self):
        if self.dev == None:
            try:
                self.dev = Colorimeter(self.port)
                self.numSamples = self.dev.getNumSamples()
                connected = True
            except Exception, e:
                QtGui.QMessageBox.critical(self,'Error', str(e))
                self.connectPushButton.setText('Connect')
                self.statusbar.showMessage('Not Connected')
                self.portLineEdit.setEnabled(True)
                connected = False
        else:
            disconnect_msg = "Disconnecting will clear all data. Continue?"
            response = self.cleanDataTable(msg=disconnect_msg)
            if response == True:
                self.connectPushButton.setText('Connect')
                try:
                    self.cleanUpAndCloseDevice()
                except Exception, e:
                    QtGui.QMessageBox.critical(self,'Error', str(e))
                self.measIndex = 0
                connected = False
            if response == False:
                connected = True

        if connected:
            self.setWidgetEnabledOnConnect()
        else:
            self.setWidgetEnabledOnDisconnect()

    def closeEvent(self,event):
        if self.dev is not None:
            self.cleanUpAndCloseDevice()
        event.accept()

    def cleanUpAndCloseDevice(self):
        self.dev.close()
        self.dev = None

    def cleanDataTable(self,setup=False,msg=''):
        if setup:
            reply = QtGui.QMessageBox.Yes
        elif len(self.tableWidget.item(0,1).text()):
            reply = QtGui.QMessageBox.question(self, 'Message', 
                             msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        else: 
            return True

        if reply == QtGui.QMessageBox.Yes:
            self.tableWidget.setRowCount(MIN_ROW_COUNT)
            self.tableWidget.setColumnCount(COL_COUNT)
            for row in range(MIN_ROW_COUNT+1):
                for col in range(COL_COUNT+1):
                    tableItem = QtGui.QTableWidgetItem()
                    tableItem.setFlags(QtCore.Qt.NoItemFlags \
                                      )
                    self.tableWidget.setItem(row,col,tableItem)
            self.measIndex = 0
            return True
        else:
            return False

    def colorRadioButton_Clicked(self,color):
        if len(self.tableWidget.item(0,1).text()):
            chn_msg = "Changing channels will clear all data. Continue?"
            response = self.cleanDataTable(msg=chn_msg)
            if not response:
                color = self.currentColor_str
                button = getattr(self,'{0}RadioButton'.format(color))
                button.setChecked(True)
        self.currentColor_str = color
        print(color)

    def plotPushButton_Clicked(self):
        print('plotPushButton_Clicked',self.measIndex)
        #dataList = []
        #for i in range(self.measIndex):
        #    tableItem = self.tableWidget.item(i,1)
        #    x = float(tableItem.text())
        #    tableItem = self.tableWidget.item(i,0)
        #    y = float(tableItem.text())
        #    dataList.append((x,y))

        #yList = [x for x,y in dataList]
        #xList = [y for x,y in dataList]
        #if len(dataList) > 1:
        #    polyFit = pylab.polyfit(xList,yList,1)
        #    xFit = pylab.linspace(min(xList), max(xList), 500)
        #    yFit = pylab.polyval(polyFit, xFit)
        #    hFit = pylab.plot(xFit,yFit,'r')
        #pylab.plot(xList,yList,'ob')
        #pylab.grid('on')
        #pylab.xlabel('Concentration')
        #pylab.ylabel('Absorbance ('+self.currentColor_str+' led)')
        #slope = polyFit[0]
        ##pylab.figlegend((hFit,),('slope = {0:1.3f}'.format(slope),), 'upper left')
        #pylab.figtext(0.15,0.85,'slope = {0:1.3f}'.format(slope), color='r')
        #pylab.show()
        
    def setWidgetEnabledOnDisconnect(self):
        self.measurePushButton.setEnabled(False)
        self.plotPushButton.setEnabled(False)
        self.clearPushButton.setEnabled(False)
        self.tableWidget.setEnabled(False)
        self.testSolutionWidget.setEnabled(False)
        self.coeffLEDWidget.setEnabled(False)
        self.portLineEdit.setEnabled(True)
        self.statusbar.showMessage('Not Connected')
        self.cleanDataTable()

    def setWidgetEnabledOnConnect(self):
        self.plotPushButton.setEnabled(True)
        self.clearPushButton.setEnabled(True)
        self.measurePushButton.setEnabled(True)
        self.testSolutionWidget.setEnabled(True)
        self.portLineEdit.setEnabled(False)
        self.connectPushButton.setFlat(False)
        self.statusbar.showMessage('Connected, Mode: Stopped')

    def measurePressed_Callback(self):
        print('measPushButton_Pressed')
        self.plotPushButton.setEnabled(False)
        self.measurePushButton.setFlat(True)
        self.statusbar.showMessage('Connected, Mode: Measuring...')

    def measureClicked_Callback(self):
        rowCount = self.measIndex+1
        if rowCount == 2:
            if not len(self.tableWidget.item(0,0).text()):
                errMsgTitle = 'Missing Value'
                errMsg = 'Concentration value not entered.'
                QtGui.QMessageBox.warning(self,errMsgTitle, errMsg)
        freq, trans, absorb = self.dev.getMeasurement()
        self.measurePushButton.setFlat(False)
        transList = []
        absorbList = []
        if self.currentColor_str=='red':
            transStr = '{0:1.2f}'.format(trans[0])
            absorbStr = '{0:1.2f}'.format(absorb[0])
            print('red: ',absorbStr)
        elif self.currentColor_str=='green':
            transStr = '{0:1.2f}'.format(trans[1])
            absorbStr = '{0:1.2f}'.format(absorb[1])
            print('green: ',absorbStr)
        elif self.currentColor_str=='blue':
            transStr = '{0:1.2f}'.format(trans[2])
            absorbStr = '{0:1.2f}'.format(absorb[2])
            print('blue: ',absorbStr)
        elif self.currentColor_str=='white':
            transStr = '{0:1.2f}'.format(trans[3])
            absorbStr = '{0:1.2f}'.format(absorb[3])
            print('white: ',absorbStr)

        transList.append(transStr)
        absorbList.append(absorbStr)

        if rowCount > MIN_ROW_COUNT:
            self.tableWidget.setRowCount(rowCount)

        tableItem = QtGui.QTableWidgetItem()
        tableItem.setText(absorbStr)
        tableItem.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(self.measIndex,1,tableItem)

        tableItem = QtGui.QTableWidgetItem()
        tableItem.setSelected(True)
        self.tableWidget.setItem(self.measIndex,0,tableItem)

        self.tableWidget.setCurrentCell(self.measIndex,0)
        self.tableWidget.editItem(self.tableWidget.currentItem()) 

        self.measIndex+=1
        self.setWidgetEnabledOnConnect()


    def clearPressed_Callback(self):
        if len(self.tableWidget.item(0,1).text()):
            self.measurePushButton.setEnabled(False)
            self.plotPushButton.setEnabled(False)
        self.clearPushButton.setFlat(True)

    def clearClicked_Callback(self):
        if len(self.tableWidget.item(0,1).text()):
            erase_msg = "Clear all data?"
            self.cleanDataTable(msg=erase_msg)
        self.clearPushButton.setFlat(False)
        self.setWidgetEnabledOnConnect()

    def main(self):
        self.show()

def measurement_gui_main():
    """
    Entry point for measurement gui
    """
    app = QtGui.QApplication(sys.argv)
    mainWindow = MeasurementMainWindow()
    mainWindow.main()
    app.exec_()


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    measurement_gui_main()

