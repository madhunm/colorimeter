# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorimeter_plot_gui.ui'
#
# Created: Tue Jul 17 16:47:57 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 618)
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
        self.ledColorWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledColorWidget.sizePolicy().hasHeightForWidth())
        self.ledColorWidget.setSizePolicy(sizePolicy)
        self.ledColorWidget.setObjectName("ledColorWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.ledColorWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.redRadioButton = QtGui.QRadioButton(self.ledColorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redRadioButton.sizePolicy().hasHeightForWidth())
        self.redRadioButton.setSizePolicy(sizePolicy)
        self.redRadioButton.setObjectName("redRadioButton")
        self.horizontalLayout_2.addWidget(self.redRadioButton)
        self.greenRadioButton = QtGui.QRadioButton(self.ledColorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenRadioButton.sizePolicy().hasHeightForWidth())
        self.greenRadioButton.setSizePolicy(sizePolicy)
        self.greenRadioButton.setObjectName("greenRadioButton")
        self.horizontalLayout_2.addWidget(self.greenRadioButton)
        self.blueRadioButton = QtGui.QRadioButton(self.ledColorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueRadioButton.sizePolicy().hasHeightForWidth())
        self.blueRadioButton.setSizePolicy(sizePolicy)
        self.blueRadioButton.setObjectName("blueRadioButton")
        self.horizontalLayout_2.addWidget(self.blueRadioButton)
        self.whiteRadioButton = QtGui.QRadioButton(self.ledColorWidget)
        self.whiteRadioButton.setObjectName("whiteRadioButton")
        self.horizontalLayout_2.addWidget(self.whiteRadioButton)
        spacerItem1 = QtGui.QSpacerItem(134, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.ledColorWidget)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = ColorimeterTableWidget(self.frame)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(True)
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
        self.calibratePushButton = QtGui.QPushButton(self.widget_3)
        self.calibratePushButton.setObjectName("calibratePushButton")
        self.horizontalLayout_3.addWidget(self.calibratePushButton)
        self.clearPushButton = QtGui.QPushButton(self.widget_3)
        self.clearPushButton.setObjectName("clearPushButton")
        self.horizontalLayout_3.addWidget(self.clearPushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.measurePushButton = QtGui.QPushButton(self.widget_3)
        self.measurePushButton.setObjectName("measurePushButton")
        self.horizontalLayout_3.addWidget(self.measurePushButton)
        self.plotPushButton = QtGui.QPushButton(self.widget_3)
        self.plotPushButton.setObjectName("plotPushButton")
        self.horizontalLayout_3.addWidget(self.plotPushButton)
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionEditTestSolutions = QtGui.QAction(MainWindow)
        self.actionEditTestSolutions.setObjectName("actionEditTestSolutions")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuOptions.addAction(self.actionExport)
        self.menuOptions.addAction(self.actionImport)
        self.menuOptions.addAction(self.actionEditTestSolutions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Colorimeter Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Serial Port", None, QtGui.QApplication.UnicodeUTF8))
        self.connectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.redRadioButton.setText(QtGui.QApplication.translate("MainWindow", "red", None, QtGui.QApplication.UnicodeUTF8))
        self.greenRadioButton.setText(QtGui.QApplication.translate("MainWindow", "green", None, QtGui.QApplication.UnicodeUTF8))
        self.blueRadioButton.setText(QtGui.QApplication.translate("MainWindow", "blue", None, QtGui.QApplication.UnicodeUTF8))
        self.whiteRadioButton.setText(QtGui.QApplication.translate("MainWindow", "white", None, QtGui.QApplication.UnicodeUTF8))
        self.calibratePushButton.setText(QtGui.QApplication.translate("MainWindow", "Calibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearPushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.measurePushButton.setText(QtGui.QApplication.translate("MainWindow", "Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.plotPushButton.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export Test Solution...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import Test Solution...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditTestSolutions.setText(QtGui.QApplication.translate("MainWindow", "Edit Test Solutions...", None, QtGui.QApplication.UnicodeUTF8))

from colorimeter_common.table_widget import ColorimeterTableWidget
