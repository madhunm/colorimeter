# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measure.ui'
#
# Created: Sat Oct 26 16:23:38 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 461)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.portLineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setMaximumSize(QtCore.QSize(140, 16777215))
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout.addWidget(self.portLineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectPushButton = QtGui.QPushButton(self.widget)
        self.connectPushButton.setObjectName("connectPushButton")
        self.horizontalLayout.addWidget(self.connectPushButton)
        self.verticalLayout.addWidget(self.widget)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.testSolutionWidget = QtGui.QWidget(self.centralwidget)
        self.testSolutionWidget.setObjectName("testSolutionWidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.testSolutionWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(self.testSolutionWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.testSolutionComboBox = QtGui.QComboBox(self.testSolutionWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testSolutionComboBox.sizePolicy().hasHeightForWidth())
        self.testSolutionComboBox.setSizePolicy(sizePolicy)
        self.testSolutionComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.testSolutionComboBox.setObjectName("testSolutionComboBox")
        self.horizontalLayout_5.addWidget(self.testSolutionComboBox)
        spacerItem1 = QtGui.QSpacerItem(461, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.testSolutionWidget)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.coeffLEDWidget = QtGui.QWidget(self.centralwidget)
        self.coeffLEDWidget.setObjectName("coeffLEDWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.coeffLEDWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.coeffLEDWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.coefficientLineEdit = QtGui.QLineEdit(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coefficientLineEdit.sizePolicy().hasHeightForWidth())
        self.coefficientLineEdit.setSizePolicy(sizePolicy)
        self.coefficientLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.coefficientLineEdit.setObjectName("coefficientLineEdit")
        self.horizontalLayout_2.addWidget(self.coefficientLineEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.coeffLEDWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.LED0RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED0RadioButton.sizePolicy().hasHeightForWidth())
        self.LED0RadioButton.setSizePolicy(sizePolicy)
        self.LED0RadioButton.setObjectName("LED0RadioButton")
        self.horizontalLayout_2.addWidget(self.LED0RadioButton)
        self.LED1RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED1RadioButton.sizePolicy().hasHeightForWidth())
        self.LED1RadioButton.setSizePolicy(sizePolicy)
        self.LED1RadioButton.setObjectName("LED1RadioButton")
        self.horizontalLayout_2.addWidget(self.LED1RadioButton)
        self.LED2RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED2RadioButton.sizePolicy().hasHeightForWidth())
        self.LED2RadioButton.setSizePolicy(sizePolicy)
        self.LED2RadioButton.setObjectName("LED2RadioButton")
        self.horizontalLayout_2.addWidget(self.LED2RadioButton)
        self.LED3RadioButton = QtGui.QRadioButton(self.coeffLEDWidget)
        self.LED3RadioButton.setObjectName("LED3RadioButton")
        self.horizontalLayout_2.addWidget(self.LED3RadioButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.coeffLEDWidget)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = ColorimeterTableWidget(self.frame)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.samplesLineEdit = QtGui.QLineEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplesLineEdit.sizePolicy().hasHeightForWidth())
        self.samplesLineEdit.setSizePolicy(sizePolicy)
        self.samplesLineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.samplesLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.samplesLineEdit.setObjectName("samplesLineEdit")
        self.horizontalLayout_3.addWidget(self.samplesLineEdit)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.calibratePushButton = QtGui.QPushButton(self.widget_3)
        self.calibratePushButton.setObjectName("calibratePushButton")
        self.horizontalLayout_3.addWidget(self.calibratePushButton)
        self.clearPushButton = QtGui.QPushButton(self.widget_3)
        self.clearPushButton.setObjectName("clearPushButton")
        self.horizontalLayout_3.addWidget(self.clearPushButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.measurePushButton = QtGui.QPushButton(self.widget_3)
        self.measurePushButton.setObjectName("measurePushButton")
        self.horizontalLayout_3.addWidget(self.measurePushButton)
        self.plotPushButton = QtGui.QPushButton(self.widget_3)
        self.plotPushButton.setObjectName("plotPushButton")
        self.horizontalLayout_3.addWidget(self.plotPushButton)
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuInclude = QtGui.QMenu(self.menuOptions)
        self.menuInclude.setObjectName("menuInclude")
        self.menuSample_Units = QtGui.QMenu(self.menuOptions)
        self.menuSample_Units.setObjectName("menuSample_Units")
        self.menuSignificantDigits = QtGui.QMenu(self.menuOptions)
        self.menuSignificantDigits.setObjectName("menuSignificantDigits")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuMode = QtGui.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReloadTestSolutions = QtGui.QAction(MainWindow)
        self.actionReloadTestSolutions.setObjectName("actionReloadTestSolutions")
        self.actionIncludeUserTestSolutions = QtGui.QAction(MainWindow)
        self.actionIncludeUserTestSolutions.setCheckable(True)
        self.actionIncludeUserTestSolutions.setObjectName("actionIncludeUserTestSolutions")
        self.actionIncludeDefaultTestSolutions = QtGui.QAction(MainWindow)
        self.actionIncludeDefaultTestSolutions.setCheckable(True)
        self.actionIncludeDefaultTestSolutions.setObjectName("actionIncludeDefaultTestSolutions")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImportTestSolution = QtGui.QAction(MainWindow)
        self.actionImportTestSolution.setObjectName("actionImportTestSolution")
        self.actionRemoveTestSolution = QtGui.QAction(MainWindow)
        self.actionRemoveTestSolution.setObjectName("actionRemoveTestSolution")
        self.actionEditTestSolutions = QtGui.QAction(MainWindow)
        self.actionEditTestSolutions.setObjectName("actionEditTestSolutions")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSampleUnitsUM = QtGui.QAction(MainWindow)
        self.actionSampleUnitsUM.setCheckable(True)
        self.actionSampleUnitsUM.setObjectName("actionSampleUnitsUM")
        self.actionSampleUnitsPPM = QtGui.QAction(MainWindow)
        self.actionSampleUnitsPPM.setCheckable(True)
        self.actionSampleUnitsPPM.setObjectName("actionSampleUnitsPPM")
        self.actionStandardRGBLED = QtGui.QAction(MainWindow)
        self.actionStandardRGBLED.setCheckable(True)
        self.actionStandardRGBLED.setObjectName("actionStandardRGBLED")
        self.actionCustomLEDVerB = QtGui.QAction(MainWindow)
        self.actionCustomLEDVerB.setCheckable(True)
        self.actionCustomLEDVerB.setObjectName("actionCustomLEDVerB")
        self.actionSignificantDigits1 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits1.setCheckable(True)
        self.actionSignificantDigits1.setObjectName("actionSignificantDigits1")
        self.actionSignificantDigits2 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits2.setCheckable(True)
        self.actionSignificantDigits2.setObjectName("actionSignificantDigits2")
        self.actionSignificantDigits3 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits3.setCheckable(True)
        self.actionSignificantDigits3.setObjectName("actionSignificantDigits3")
        self.actionSignificantDigits4 = QtGui.QAction(MainWindow)
        self.actionSignificantDigits4.setCheckable(True)
        self.actionSignificantDigits4.setObjectName("actionSignificantDigits4")
        self.actionCustomLEDVerC = QtGui.QAction(MainWindow)
        self.actionCustomLEDVerC.setCheckable(True)
        self.actionCustomLEDVerC.setObjectName("actionCustomLEDVerC")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuInclude.addAction(self.actionIncludeUserTestSolutions)
        self.menuInclude.addAction(self.actionIncludeDefaultTestSolutions)
        self.menuSample_Units.addAction(self.actionSampleUnitsUM)
        self.menuSample_Units.addAction(self.actionSampleUnitsPPM)
        self.menuOptions.addAction(self.menuSample_Units.menuAction())
        self.menuOptions.addAction(self.menuSignificantDigits.menuAction())
        self.menuOptions.addAction(self.menuInclude.menuAction())
        self.menuOptions.addAction(self.actionEditTestSolutions)
        self.menu_Help.addAction(self.actionAbout)
        self.menuMode.addAction(self.actionStandardRGBLED)
        self.menuMode.addAction(self.actionCustomLEDVerB)
        self.menuMode.addAction(self.actionCustomLEDVerC)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Colorimeter Measurement", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Serial Port", None, QtGui.QApplication.UnicodeUTF8))
        self.connectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Test Solution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Coefficient", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "LED", None, QtGui.QApplication.UnicodeUTF8))
        self.LED0RadioButton.setText(QtGui.QApplication.translate("MainWindow", "LED0", None, QtGui.QApplication.UnicodeUTF8))
        self.LED1RadioButton.setText(QtGui.QApplication.translate("MainWindow", "LED1", None, QtGui.QApplication.UnicodeUTF8))
        self.LED2RadioButton.setText(QtGui.QApplication.translate("MainWindow", "LED2", None, QtGui.QApplication.UnicodeUTF8))
        self.LED3RadioButton.setText(QtGui.QApplication.translate("MainWindow", "LED3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Samples", None, QtGui.QApplication.UnicodeUTF8))
        self.calibratePushButton.setText(QtGui.QApplication.translate("MainWindow", "Calibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearPushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.measurePushButton.setText(QtGui.QApplication.translate("MainWindow", "Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.plotPushButton.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInclude.setTitle(QtGui.QApplication.translate("MainWindow", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSample_Units.setTitle(QtGui.QApplication.translate("MainWindow", "Sample Units", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSignificantDigits.setTitle(QtGui.QApplication.translate("MainWindow", "Significant Digits", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMode.setTitle(QtGui.QApplication.translate("MainWindow", "&Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReloadTestSolutions.setText(QtGui.QApplication.translate("MainWindow", "Reload Test Solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncludeUserTestSolutions.setText(QtGui.QApplication.translate("MainWindow", "User Test Solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncludeDefaultTestSolutions.setText(QtGui.QApplication.translate("MainWindow", "Default Test Solutions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportTestSolution.setText(QtGui.QApplication.translate("MainWindow", "Import Test Solution...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveTestSolution.setText(QtGui.QApplication.translate("MainWindow", "Remove Test Solution...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditTestSolutions.setText(QtGui.QApplication.translate("MainWindow", "Edit User Test Solutions...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSampleUnitsUM.setText(QtGui.QApplication.translate("MainWindow", "uM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSampleUnitsPPM.setText(QtGui.QApplication.translate("MainWindow", "ppm", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStandardRGBLED.setText(QtGui.QApplication.translate("MainWindow", "Standard RGB LED", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCustomLEDVerB.setText(QtGui.QApplication.translate("MainWindow", "One custom LED (Ver. B)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignificantDigits1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignificantDigits2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignificantDigits3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignificantDigits4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCustomLEDVerC.setText(QtGui.QApplication.translate("MainWindow", "Two custom LEDs (Ver. C)", None, QtGui.QApplication.UnicodeUTF8))

from colorimeter.table_widget import ColorimeterTableWidget
