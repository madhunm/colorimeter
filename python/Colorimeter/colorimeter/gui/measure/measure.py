from __future__ import print_function
import os 
import sys 
import random 
import time
import numpy
import random
import matplotlib
import matplotlib.pyplot as plt 
plt.ion()

from PyQt4 import QtCore
from PyQt4 import QtGui

from measure_ui import Ui_MainWindow 
from colorimeter import constants 
from colorimeter import import_export 
from colorimeter import standard_curve
from colorimeter.main_window import MainWindowWithTable

class MeasureMainWindow(MainWindowWithTable, Ui_MainWindow):

    def __init__(self,parent=None):
        super(MeasureMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.connectActions()

    def connectActions(self):
        super(MeasureMainWindow,self).connectActions()
        self.testSolutionComboBox.currentIndexChanged.connect(
                self.testSolutionChanged_Callback
                )
        self.actionIncludeDefaultTestSolutions.toggled.connect(
                self.populateTestSolutionComboBox
                )
        self.actionIncludeUserTestSolutions.toggled.connect(
                self.populateTestSolutionComboBox
                )

    def initialize(self):
        super(MeasureMainWindow,self).initialize()
        self.coeff = None
        self.noValueSymbol = constants.NO_VALUE_SYMBOL_LABEL

        # Set up data table
        self.tableWidget.clean(setup=True)
        self.tableWidget.updateFunc = self.updatePlot
        concentrationStr = QtCore.QString.fromUtf8("Concentration (\xc2\xb5M)")
        self.tableWidget.setHorizontalHeaderLabels(('Sample', concentrationStr)) 

        # Set startup state for including test solution.
        self.actionIncludeDefaultTestSolutions.setChecked(True)
        self.actionIncludeUserTestSolutions.setChecked(True)
        self.updateTestSolutionDicts()
        self.populateTestSolutionComboBox()
        self.testSolutionComboBox.setCurrentIndex(1)
        self.updateWidgetEnabled()

    def editTestSolutions_Callback(self):
        changed = super(MeasureMainWindow,self).editTestSolutions_Callback()
        if changed:
            self.updateTestSolutionDicts()
            self.populateTestSolutionComboBox()

    def testSolutionChanged_Callback(self,index):
        self.updateTestSolution(index)

    def updateTestSolution(self,index):
        if index <= 0:
            self.coeffLEDWidget.setEnabled(True)
            self.coefficientLineEdit.setText("")
            self.coeff = None
        else:
            self.coeffLEDWidget.setEnabled(False)
            itemText = str(self.testSolutionComboBox.itemText(index))
            testSolutionDict = {}
            testSolutionDict.update(self.user_TestSolutionDict)
            testSolutionDict.update(self.default_TestSolutionDict)
            pathName = testSolutionDict[itemText]
            data = import_export.importTestSolutionData(pathName)
            self.coeff = getCoefficientFromData(data)
            self.coefficientLineEdit.setText('{0:1.1f}'.format(1.0e6*self.coeff))
            self.setLEDColor(data['led'])
        self.updateWidgetEnabled()

    def getMeasurement(self):
        ledNumber = constants.COLOR2LED_DICT[self.currentColor]
        if constants.DEVEL_FAKE_MEASURE:  
            conc = random.random()
        else:
            freq, trans, absorb = self.dev.getMeasurement()
            conc = absorb[ledNumber]/self.coeff

        concStr = '{0:1.2f}'.format(conc)
        self.measurePushButton.setFlat(False)
        self.tableWidget.addData('',concStr,selectAndEdit=True)

    def getSaveFileHeader(self):
        timeStr = time.strftime('%Y-%m-%d %H:%M:%S %Z') 
        headerList = [ 
                '# {0}'.format(timeStr), 
                '# Colorimeter Data', 
                '# LED {0}'.format(self.currentColor),
                '# ----------------------------', 
                '# Label    |    Concentration ',
                ]
        headerStr = os.linesep.join(headerList)
        return headerStr

    def updateWidgetEnabled(self):
        super(MeasureMainWindow,self).updateWidgetEnabled()
        if self.dev is None:
            self.testSolutionWidget.setEnabled(False)
            self.coeffLEDWidget.setEnabled(False)
        else:
            self.testSolutionWidget.setEnabled(True)
            if self.coeff is None:
                self.calibratePushButton.setEnabled(False)
            else:
                self.calibratePushButton.setEnabled(True)

    def updatePlot(self,create=False):
        # Only create new figure is asked to do so
        if not create and not plt.fignum_exists(constants.PLOT_FIGURE_NUM):
            return
        # Check if there is any data to plot
        dataList = self.tableWidget.getData()
        dataList = dataListToLabelAndFloat(dataList)
        if not dataList:
            self.closeFigure()
            return 
        # Unpack data and create plot 
        labelList, concList = zip(*dataList)
        posList = range(1,len(concList)+1)
        xlim = (
                posList[0]  - 0.5*constants.PLOT_BAR_WIDTH, 
                posList[-1] + 1.5*constants.PLOT_BAR_WIDTH,
                )
        ylim = (0,constants.PLOT_YLIM_ADJUST*max(concList))
        plt.clf()
        self.fig = plt.figure(constants.PLOT_FIGURE_NUM)
        self.fig.canvas.manager.set_window_title('Colorimeter Measurement: Concentration Plot')
        ax = self.fig.add_subplot(111)
        ax.bar(posList,concList,width=constants.PLOT_BAR_WIDTH,color='b',linewidth=2)

        for pos, value in zip(posList, concList): 
            textXPos = pos + 0.5*constants.PLOT_BAR_WIDTH
            textYPos = value + constants.PLOT_TEXT_Y_OFFSET
            valueStr = '{0:1.3f}'.format(value)
            ax.text(textXPos,textYPos, valueStr, ha ='center', va ='bottom') 

        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_xticks([x+0.5*constants.PLOT_BAR_WIDTH for x in posList])
        ax.set_xticklabels(labelList)
        ax.set_ylabel('Concentration')
        ax.set_xlabel('Samples')
        plt.draw() 

    def updateTestSolutionDicts(self):
        self.user_TestSolutionDict = self.loadUserTestSolutionDict()
        self.default_TestSolutionDict = self.loadDefaultTestSolutionDict()

    def loadDefaultTestSolutionDict(self):
        return import_export.loadDefaultTestSolutionDict()

    def loadUserTestSolutionDict(self):
        userTestSolutionDir = import_export.getUserTestSolutionDir(self.userHome)
        fileList = import_export.getTestSolutionFilesFromDir(userTestSolutionDir)
        return import_export.loadTestSolutionDict(fileList,tag='U')

    def populateTestSolutionComboBox(self):
        self.testSolutionComboBox.clear()
        self.testSolutionComboBox.addItem('-- (manually specify) --')
        includeDflt = self.actionIncludeDefaultTestSolutions.isChecked()
        includeUser = self.actionIncludeUserTestSolutions.isChecked()

        # Add default test solutions
        if includeDflt:
            for name in sorted(self.default_TestSolutionDict):
                self.testSolutionComboBox.addItem(name)

        if includeDflt and includeUser:
            count = self.testSolutionComboBox.count()+1
            self.testSolutionComboBox.insertSeparator(count)

        # Add user test solutions
        if includeUser:
            for name in sorted(self.user_TestSolutionDict):
                self.testSolutionComboBox.addItem(name)

        index = min([1,self.testSolutionComboBox.count()-1])
        self.testSolutionComboBox.setCurrentIndex(index)
        self.updateTestSolution(index)

    def setTableData(self,dataList):
        dataList = dataListToLabelAndFloat(dataList)
        self.tableWidget.clean(setup=True)
        for label, conc in dataList:
            if label == self.noValueSymbol:
                label = ''
            else:
                label = str(label)
            conc = str(conc)
            self.tableWidget.addData(label,conc)
        pass

def dataListToLabelAndFloat(dataList):
    dataListNew = []
    for x,y in dataList:
        try: 
            y = float(y)
        except ValueError:
            continue
        dataListNew.append((x,y))
    return dataListNew

def getCoefficientFromData(data): 
    values = data['values']
    abso, conc = zip(*values)
    coeff = standard_curve.getCoefficient(abso,conc,fitType=constants.FIT_TYPE)
    return coeff

def startMeasureGUI():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MeasureMainWindow()
    mainWindow.main()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    startMeasureGUI()
