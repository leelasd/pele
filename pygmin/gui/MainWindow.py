# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jun  4 09:24:41 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(681, 566)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.BHTab = QtGui.QWidget()
        self.BHTab.setObjectName(_fromUtf8("BHTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.BHTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget = Show3D(self.BHTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listWidget = QtGui.QListWidget(self.BHTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_3.addWidget(self.listWidget)
        self.btnRun = QtGui.QPushButton(self.BHTab)
        self.btnRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.verticalLayout_3.addWidget(self.btnRun)
        self.btnPause = QtGui.QPushButton(self.BHTab)
        self.btnPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPause.setObjectName(_fromUtf8("btnPause"))
        self.verticalLayout_3.addWidget(self.btnPause)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.BHTab, _fromUtf8(""))
        self.NEBTab = QtGui.QWidget()
        self.NEBTab.setObjectName(_fromUtf8("NEBTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.NEBTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.oglPath = Show3D(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oglPath.sizePolicy().hasHeightForWidth())
        self.oglPath.setSizePolicy(sizePolicy)
        self.oglPath.setObjectName(_fromUtf8("oglPath"))
        self.gridLayout_4.addWidget(self.oglPath, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.listMinima1 = QtGui.QListWidget(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listMinima1.sizePolicy().hasHeightForWidth())
        self.listMinima1.setSizePolicy(sizePolicy)
        self.listMinima1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listMinima1.setObjectName(_fromUtf8("listMinima1"))
        self.verticalLayout_5.addWidget(self.listMinima1)
        self.listMinima2 = QtGui.QListWidget(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listMinima2.sizePolicy().hasHeightForWidth())
        self.listMinima2.setSizePolicy(sizePolicy)
        self.listMinima2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listMinima2.setObjectName(_fromUtf8("listMinima2"))
        self.verticalLayout_5.addWidget(self.listMinima2)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 3, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(20, 0, 20, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnConnect = QtGui.QPushButton(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConnect.sizePolicy().hasHeightForWidth())
        self.btnConnect.setSizePolicy(sizePolicy)
        self.btnConnect.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.gridLayout_2.addWidget(self.btnConnect, 0, 1, 1, 1)
        self.btnAlign = QtGui.QPushButton(self.NEBTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAlign.sizePolicy().hasHeightForWidth())
        self.btnAlign.setSizePolicy(sizePolicy)
        self.btnAlign.setMaximumSize(QtCore.QSize(100, 100))
        self.btnAlign.setText(QtGui.QApplication.translate("MainWindow", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAlign.setObjectName(_fromUtf8("btnAlign"))
        self.gridLayout_2.addWidget(self.btnAlign, 0, 0, 1, 1)
        self.btnEnergies = QtGui.QPushButton(self.NEBTab)
        self.btnEnergies.setText(QtGui.QApplication.translate("MainWindow", "Energies", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEnergies.setObjectName(_fromUtf8("btnEnergies"))
        self.gridLayout_2.addWidget(self.btnEnergies, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 3, 1, 1)
        self.sliderFrame = QtGui.QSlider(self.NEBTab)
        self.sliderFrame.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFrame.setObjectName(_fromUtf8("sliderFrame"))
        self.gridLayout_4.addWidget(self.sliderFrame, 1, 0, 1, 1)
        self.tabWidget.addTab(self.NEBTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSimulation = QtGui.QMenu(self.menubar)
        self.menuSimulation.setTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSimulation.setObjectName(_fromUtf8("menuSimulation"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuSimulation.addAction(self.actionNew)
        self.menuSimulation.addAction(self.actionSave)
        self.menuSimulation.addAction(self.actionLoad)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.SelectMinimum)
        QtCore.QObject.connect(self.btnRun, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.StartBasinHopping)
        QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.NewSystem)
        QtCore.QObject.connect(self.btnAlign, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.AlignMinima)
        QtCore.QObject.connect(self.btnConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ConnectMinima)
        QtCore.QObject.connect(self.listMinima1, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.SelectMinimum1)
        QtCore.QObject.connect(self.listMinima2, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.SelectMinimum2)
        QtCore.QObject.connect(self.sliderFrame, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), MainWindow.showFrame)
        QtCore.QObject.connect(self.btnEnergies, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.showEnergies)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.save)
        QtCore.QObject.connect(self.actionLoad, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.load)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.listWidget.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BHTab), QtGui.QApplication.translate("MainWindow", "Basin Hopping", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NEBTab), QtGui.QApplication.translate("MainWindow", "NEB", None, QtGui.QApplication.UnicodeUTF8))

from show3d import Show3D