# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measure.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.portLineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setMaximumSize(QtCore.QSize(140, 16777215))
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout.addWidget(self.portLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectPushButton = QtWidgets.QPushButton(self.widget)
        self.connectPushButton.setObjectName("connectPushButton")
        self.horizontalLayout.addWidget(self.connectPushButton)
        self.verticalLayout.addWidget(self.widget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.testSolutionWidget = QtWidgets.QWidget(self.centralwidget)
        self.testSolutionWidget.setObjectName("testSolutionWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.testSolutionWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.testSolutionWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.testSolutionComboBox = QtWidgets.QComboBox(self.testSolutionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testSolutionComboBox.sizePolicy().hasHeightForWidth())
        self.testSolutionComboBox.setSizePolicy(sizePolicy)
        self.testSolutionComboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.testSolutionComboBox.setObjectName("testSolutionComboBox")
        self.horizontalLayout_5.addWidget(self.testSolutionComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(461, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.testSolutionWidget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.coeffLEDWidget = QtWidgets.QWidget(self.centralwidget)
        self.coeffLEDWidget.setObjectName("coeffLEDWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.coeffLEDWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.coeffLEDWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.coefficientLineEdit = QtWidgets.QLineEdit(self.coeffLEDWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coefficientLineEdit.sizePolicy().hasHeightForWidth())
        self.coefficientLineEdit.setSizePolicy(sizePolicy)
        self.coefficientLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.coefficientLineEdit.setObjectName("coefficientLineEdit")
        self.horizontalLayout_2.addWidget(self.coefficientLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.coeffLEDWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.LED0RadioButton = QtWidgets.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED0RadioButton.sizePolicy().hasHeightForWidth())
        self.LED0RadioButton.setSizePolicy(sizePolicy)
        self.LED0RadioButton.setObjectName("LED0RadioButton")
        self.horizontalLayout_2.addWidget(self.LED0RadioButton)
        self.LED1RadioButton = QtWidgets.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED1RadioButton.sizePolicy().hasHeightForWidth())
        self.LED1RadioButton.setSizePolicy(sizePolicy)
        self.LED1RadioButton.setObjectName("LED1RadioButton")
        self.horizontalLayout_2.addWidget(self.LED1RadioButton)
        self.LED2RadioButton = QtWidgets.QRadioButton(self.coeffLEDWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LED2RadioButton.sizePolicy().hasHeightForWidth())
        self.LED2RadioButton.setSizePolicy(sizePolicy)
        self.LED2RadioButton.setObjectName("LED2RadioButton")
        self.horizontalLayout_2.addWidget(self.LED2RadioButton)
        self.LED3RadioButton = QtWidgets.QRadioButton(self.coeffLEDWidget)
        self.LED3RadioButton.setObjectName("LED3RadioButton")
        self.horizontalLayout_2.addWidget(self.LED3RadioButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.coeffLEDWidget)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = ColorimeterTableWidget(self.frame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.samplesLineEdit = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.samplesLineEdit.sizePolicy().hasHeightForWidth())
        self.samplesLineEdit.setSizePolicy(sizePolicy)
        self.samplesLineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.samplesLineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.samplesLineEdit.setObjectName("samplesLineEdit")
        self.horizontalLayout_3.addWidget(self.samplesLineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.calibratePushButton = QtWidgets.QPushButton(self.widget_3)
        self.calibratePushButton.setObjectName("calibratePushButton")
        self.horizontalLayout_3.addWidget(self.calibratePushButton)
        self.clearPushButton = QtWidgets.QPushButton(self.widget_3)
        self.clearPushButton.setObjectName("clearPushButton")
        self.horizontalLayout_3.addWidget(self.clearPushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.measurePushButton = QtWidgets.QPushButton(self.widget_3)
        self.measurePushButton.setObjectName("measurePushButton")
        self.horizontalLayout_3.addWidget(self.measurePushButton)
        self.plotPushButton = QtWidgets.QPushButton(self.widget_3)
        self.plotPushButton.setObjectName("plotPushButton")
        self.horizontalLayout_3.addWidget(self.plotPushButton)
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuInclude = QtWidgets.QMenu(self.menuOptions)
        self.menuInclude.setObjectName("menuInclude")
        self.menuSignificantDigits = QtWidgets.QMenu(self.menuOptions)
        self.menuSignificantDigits.setObjectName("menuSignificantDigits")
        self.menuSample_Units = QtWidgets.QMenu(self.menuOptions)
        self.menuSample_Units.setObjectName("menuSample_Units")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReloadTestSolutions = QtWidgets.QAction(MainWindow)
        self.actionReloadTestSolutions.setObjectName("actionReloadTestSolutions")
        self.actionIncludeUserTestSolutions = QtWidgets.QAction(MainWindow)
        self.actionIncludeUserTestSolutions.setCheckable(True)
        self.actionIncludeUserTestSolutions.setObjectName("actionIncludeUserTestSolutions")
        self.actionIncludeDefaultTestSolutions = QtWidgets.QAction(MainWindow)
        self.actionIncludeDefaultTestSolutions.setCheckable(True)
        self.actionIncludeDefaultTestSolutions.setObjectName("actionIncludeDefaultTestSolutions")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImportTestSolution = QtWidgets.QAction(MainWindow)
        self.actionImportTestSolution.setObjectName("actionImportTestSolution")
        self.actionRemoveTestSolution = QtWidgets.QAction(MainWindow)
        self.actionRemoveTestSolution.setObjectName("actionRemoveTestSolution")
        self.actionEditTestSolutions = QtWidgets.QAction(MainWindow)
        self.actionEditTestSolutions.setObjectName("actionEditTestSolutions")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSampleUnitsUM = QtWidgets.QAction(MainWindow)
        self.actionSampleUnitsUM.setCheckable(True)
        self.actionSampleUnitsUM.setObjectName("actionSampleUnitsUM")
        self.actionSampleUnitsPPM = QtWidgets.QAction(MainWindow)
        self.actionSampleUnitsPPM.setCheckable(True)
        self.actionSampleUnitsPPM.setObjectName("actionSampleUnitsPPM")
        self.actionStandardRGBLED = QtWidgets.QAction(MainWindow)
        self.actionStandardRGBLED.setCheckable(True)
        self.actionStandardRGBLED.setObjectName("actionStandardRGBLED")
        self.actionCustomLEDVerB = QtWidgets.QAction(MainWindow)
        self.actionCustomLEDVerB.setCheckable(True)
        self.actionCustomLEDVerB.setObjectName("actionCustomLEDVerB")
        self.actionSignificantDigits1 = QtWidgets.QAction(MainWindow)
        self.actionSignificantDigits1.setCheckable(True)
        self.actionSignificantDigits1.setObjectName("actionSignificantDigits1")
        self.actionSignificantDigits2 = QtWidgets.QAction(MainWindow)
        self.actionSignificantDigits2.setCheckable(True)
        self.actionSignificantDigits2.setObjectName("actionSignificantDigits2")
        self.actionSignificantDigits3 = QtWidgets.QAction(MainWindow)
        self.actionSignificantDigits3.setCheckable(True)
        self.actionSignificantDigits3.setObjectName("actionSignificantDigits3")
        self.actionSignificantDigits4 = QtWidgets.QAction(MainWindow)
        self.actionSignificantDigits4.setCheckable(True)
        self.actionSignificantDigits4.setObjectName("actionSignificantDigits4")
        self.actionCustomLEDVerC = QtWidgets.QAction(MainWindow)
        self.actionCustomLEDVerC.setCheckable(True)
        self.actionCustomLEDVerC.setObjectName("actionCustomLEDVerC")
        self.actionSampleUnitsPH = QtWidgets.QAction(MainWindow)
        self.actionSampleUnitsPH.setCheckable(True)
        self.actionSampleUnitsPH.setObjectName("actionSampleUnitsPH")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuInclude.addAction(self.actionIncludeUserTestSolutions)
        self.menuInclude.addAction(self.actionIncludeDefaultTestSolutions)
        self.menuSample_Units.addAction(self.actionSampleUnitsUM)
        self.menuSample_Units.addAction(self.actionSampleUnitsPPM)
        self.menuSample_Units.addAction(self.actionSampleUnitsPH)
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Colorimeter Measurement"))
        self.label.setText(_translate("MainWindow", "Serial Port"))
        self.connectPushButton.setText(_translate("MainWindow", "Connect"))
        self.label_4.setText(_translate("MainWindow", "Test Solution"))
        self.label_2.setText(_translate("MainWindow", "Coefficient"))
        self.label_3.setText(_translate("MainWindow", "LED"))
        self.LED0RadioButton.setText(_translate("MainWindow", "LED0"))
        self.LED1RadioButton.setText(_translate("MainWindow", "LED1"))
        self.LED2RadioButton.setText(_translate("MainWindow", "LED2"))
        self.LED3RadioButton.setText(_translate("MainWindow", "LED3"))
        self.label_5.setText(_translate("MainWindow", "Samples"))
        self.calibratePushButton.setText(_translate("MainWindow", "Calibrate"))
        self.clearPushButton.setText(_translate("MainWindow", "Clear"))
        self.measurePushButton.setText(_translate("MainWindow", "Measure"))
        self.plotPushButton.setText(_translate("MainWindow", "Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuOptions.setTitle(_translate("MainWindow", "&Options"))
        self.menuInclude.setTitle(_translate("MainWindow", "Include"))
        self.menuSignificantDigits.setTitle(_translate("MainWindow", "Significant Digits"))
        self.menuSample_Units.setTitle(_translate("MainWindow", "Sample Units"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menuMode.setTitle(_translate("MainWindow", "&Mode"))
        self.actionReloadTestSolutions.setText(_translate("MainWindow", "Reload Test Solutions"))
        self.actionIncludeUserTestSolutions.setText(_translate("MainWindow", "User Test Solutions"))
        self.actionIncludeDefaultTestSolutions.setText(_translate("MainWindow", "Default Test Solutions"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionImportTestSolution.setText(_translate("MainWindow", "Import Test Solution..."))
        self.actionRemoveTestSolution.setText(_translate("MainWindow", "Remove Test Solution..."))
        self.actionEditTestSolutions.setText(_translate("MainWindow", "Edit User Test Solutions..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSampleUnitsUM.setText(_translate("MainWindow", "uM"))
        self.actionSampleUnitsPPM.setText(_translate("MainWindow", "ppm"))
        self.actionStandardRGBLED.setText(_translate("MainWindow", "Standard RGB LED"))
        self.actionCustomLEDVerB.setText(_translate("MainWindow", "One custom LED (Ver. B)"))
        self.actionSignificantDigits1.setText(_translate("MainWindow", "1"))
        self.actionSignificantDigits2.setText(_translate("MainWindow", "2"))
        self.actionSignificantDigits3.setText(_translate("MainWindow", "3"))
        self.actionSignificantDigits4.setText(_translate("MainWindow", "4"))
        self.actionCustomLEDVerC.setText(_translate("MainWindow", "Two custom LEDs (Ver. C)"))
        self.actionSampleUnitsPH.setText(_translate("MainWindow", "pH"))

from colorimeter.table_widget import ColorimeterTableWidget
