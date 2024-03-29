# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NSEUIMAINWINDOW.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import CalculationUI
from NIFTY50.StoreDataIntoDataBaseNIFTY50 import StoreIntoDatabaseNifity50
from NIFTY50.DownloadDataFromWebNIFTY50 import DownloadDataFromWebNIFTY50
from NIFTY50FROMNIFTYALL  import Nifty50FromNiftyAll
from StoreDataIntoDataBaseNIFTYALL import StoreIntoDatabaseNiftyAll
from CheckForRemainingDayNiftyAll import CheckForRemainingDayNiftyAll
from UpdateDataNiftyAllForRemainingDays import UpdateDataNiftyAllForRemainingDays

from CalculationUI import CalculationUi_MainWindow

'''
Script for UI Design of Technical Analysis of National Stock Exchange
'''

class Ui_MainWindow(object):

    def openCalculationUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = CalculationUi_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblHeading = QtWidgets.QLabel(self.centralwidget)
        self.lblHeading.setGeometry(QtCore.QRect(10, 10, 909, 109))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeading.setFont(font)
        self.lblHeading.setStyleSheet("background-color: rgb(140, 244, 255)")
        self.lblHeading.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeading.setObjectName("lblHeading")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 911, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnNiftyAll = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNiftyAll.sizePolicy().hasHeightForWidth())
        self.btnNiftyAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnNiftyAll.setFont(font)
        self.btnNiftyAll.setStyleSheet("")
        self.btnNiftyAll.setObjectName("btnNiftyAll")
        self.verticalLayout_3.addWidget(self.btnNiftyAll)
        self.btnNifty50 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNifty50.sizePolicy().hasHeightForWidth())
        self.btnNifty50.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnNifty50.setFont(font)
        self.btnNifty50.setStyleSheet("")
        self.btnNifty50.setObjectName("btnNifty50")
        self.verticalLayout_3.addWidget(self.btnNifty50)
        self.btnNifty50FromNiftyAll = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNifty50FromNiftyAll.sizePolicy().hasHeightForWidth())
        self.btnNifty50FromNiftyAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnNifty50FromNiftyAll.setFont(font)
        self.btnNifty50FromNiftyAll.setStyleSheet("")
        self.btnNifty50FromNiftyAll.setObjectName("btnNifty50FromNiftyAll")
        self.verticalLayout_3.addWidget(self.btnNifty50FromNiftyAll)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnRemainingDayNiftyAll = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemainingDayNiftyAll.sizePolicy().hasHeightForWidth())
        self.btnRemainingDayNiftyAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnRemainingDayNiftyAll.setFont(font)
        self.btnRemainingDayNiftyAll.setStyleSheet("")
        self.btnRemainingDayNiftyAll.setObjectName("btnRemainingDayNiftyAll")
        self.verticalLayout_4.addWidget(self.btnRemainingDayNiftyAll)
        self.btnUpdateDataNiftyAll = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdateDataNiftyAll.sizePolicy().hasHeightForWidth())
        self.btnUpdateDataNiftyAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnUpdateDataNiftyAll.setFont(font)
        self.btnUpdateDataNiftyAll.setStyleSheet("")
        self.btnUpdateDataNiftyAll.setObjectName("btnUpdateDataNiftyAll")
        self.verticalLayout_4.addWidget(self.btnUpdateDataNiftyAll)
        self.btnDownloadNifty50 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDownloadNifty50.sizePolicy().hasHeightForWidth())
        self.btnDownloadNifty50.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnDownloadNifty50.setFont(font)
        self.btnDownloadNifty50.setStyleSheet("")
        self.btnDownloadNifty50.setObjectName("btnDownloadNifty50")
        self.verticalLayout_4.addWidget(self.btnDownloadNifty50)
        self.btnCalculation = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalculation.sizePolicy().hasHeightForWidth())
        self.btnCalculation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnCalculation.setFont(font)
        self.btnCalculation.setStyleSheet("")
        self.btnCalculation.setObjectName("btnCalculation")
        self.verticalLayout_4.addWidget(self.btnCalculation)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        # Connecting Buttons
        self.objNifity50 = StoreIntoDatabaseNifity50()
        self.btnNifty50.clicked.connect(self.objNifity50.executeStore)

        self.objDownloadNifty50 = DownloadDataFromWebNIFTY50()
        self.btnDownloadNifty50.clicked.connect(self.objDownloadNifty50.downloadNifty50)

        self.objNifty50FromNiftyAll = Nifty50FromNiftyAll()
        self.btnNifty50FromNiftyAll.clicked.connect(self.objNifty50FromNiftyAll.copyData)

        self.objNiftyAll = StoreIntoDatabaseNiftyAll()
        self.btnNiftyAll.clicked.connect(self.objNiftyAll.executeStoreNiftyAll)

        self.objCheckRemaining = CheckForRemainingDayNiftyAll()
        self.btnRemainingDayNiftyAll.clicked.connect(self.objCheckRemaining.remainingDayData)

        self.objUpdateNiftyAll = UpdateDataNiftyAllForRemainingDays()
        self.btnUpdateDataNiftyAll.clicked.connect(self.objUpdateNiftyAll.executeUpdateNiftyAll)

        self.btnCalculation.clicked.connect(self.openCalculationUI)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Technical Analysis of National Stock Exchange"))
        self.lblHeading.setText(_translate("MainWindow", "Technical Analysis of National Stock Exchange"))
        self.btnNiftyAll.setText(_translate("MainWindow", "Nifty All"))
        self.btnNifty50.setText(_translate("MainWindow", "NIFTY 50"))
        self.btnNifty50FromNiftyAll.setText(_translate("MainWindow", "NIFTY 50 FROM NIFTY ALL"))
        self.btnRemainingDayNiftyAll.setText(_translate("MainWindow", "Check For Remaining Days Nifty All"))
        self.btnUpdateDataNiftyAll.setText(_translate("MainWindow", "Update Daya Nifty All For Remaining Days"))
        self.btnDownloadNifty50.setText(_translate("MainWindow", "Download NIFTY 50"))
        self.btnCalculation.setText(_translate("MainWindow", "CALCULATION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

