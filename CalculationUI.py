# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from CalculatingLast5Days import CalculatingLast5Days
from PyQt5 import QtCore, QtGui, QtWidgets

class CalculationUi_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 444)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnlast5days = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlast5days.sizePolicy().hasHeightForWidth())
        self.btnlast5days.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnlast5days.setFont(font)
        self.btnlast5days.setStyleSheet("")
        self.btnlast5days.setObjectName("btnlast5days")
        self.verticalLayout_6.addWidget(self.btnlast5days)
        self.btnlast2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlast2.sizePolicy().hasHeightForWidth())
        self.btnlast2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnlast2.setFont(font)
        self.btnlast2.setStyleSheet("")
        self.btnlast2.setObjectName("btnlast2")
        self.verticalLayout_6.addWidget(self.btnlast2)
        self.btnNifty50FromNiftyAll_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNifty50FromNiftyAll_3.sizePolicy().hasHeightForWidth())
        self.btnNifty50FromNiftyAll_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnNifty50FromNiftyAll_3.setFont(font)
        self.btnNifty50FromNiftyAll_3.setStyleSheet("")
        self.btnNifty50FromNiftyAll_3.setObjectName("btnNifty50FromNiftyAll_3")
        self.verticalLayout_6.addWidget(self.btnNifty50FromNiftyAll_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btnlast1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlast1.sizePolicy().hasHeightForWidth())
        self.btnlast1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnlast1.setFont(font)
        self.btnlast1.setStyleSheet("")
        self.btnlast1.setObjectName("btnlast1")
        self.verticalLayout_7.addWidget(self.btnlast1)
        self.btnlast4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlast4.sizePolicy().hasHeightForWidth())
        self.btnlast4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnlast4.setFont(font)
        self.btnlast4.setStyleSheet("")
        self.btnlast4.setObjectName("btnlast4")
        self.verticalLayout_7.addWidget(self.btnlast4)
        self.btnlast5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnlast5.sizePolicy().hasHeightForWidth())
        self.btnlast5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnlast5.setFont(font)
        self.btnlast5.setStyleSheet("")
        self.btnlast5.setObjectName("btnlast5")
        self.verticalLayout_7.addWidget(self.btnlast5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)

        # Calling Function
        self.objCalculation = CalculatingLast5Days()
        self.btnlast5days.clicked.connect(self.objCalculation.calculatingData)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblHeading.setText(_translate("MainWindow", "Calulation of NSE Data"))
        self.btnlast5days.setText(_translate("MainWindow", "Last 5 Days"))
        self.btnlast2.setText(_translate("MainWindow", "Last "))
        self.btnNifty50FromNiftyAll_3.setText(_translate("MainWindow", "Last "))
        self.btnlast1.setText(_translate("MainWindow", "Last"))
        self.btnlast4.setText(_translate("MainWindow", "Last "))
        self.btnlast5.setText(_translate("MainWindow", "Last "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CalculationUi_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

