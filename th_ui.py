# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'th.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1083, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("DNA.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 991, 621))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setMaximumSize(QtCore.QSize(150, 100))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout.addWidget(self.textEdit_3, 4, 6, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 7, 3, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(150, 100))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 3, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 6, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 5, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(150, 100))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 3, 6, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setMaximumSize(QtCore.QSize(50000, 50000))
        self.groupBox.setAcceptDrops(True)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 10, 91, 18))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 10, 112, 18))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setAcceptDrops(True)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(0, 10, 112, 18))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(110, 10, 112, 18))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout.addWidget(self.groupBox_2, 2, 4, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 5, 1, 1)
        self.listWidget = QtGui.QListWidget(self.gridLayoutWidget)
        self.listWidget.setMaximumSize(QtCore.QSize(250, 250))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 4, 3, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tophat", None))
        self.pushButton_3.setText(_translate("MainWindow", "Download DNA File", None))
        self.label_7.setText(_translate("MainWindow", "Annotation File", None))
        self.label_3.setText(_translate("MainWindow", "Do you want to use annotation file?", None))
        self.label_5.setText(_translate("MainWindow", "R2 Files", None))
        self.label_4.setText(_translate("MainWindow", "R1 Files", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_6.setText(_translate("MainWindow", "Abort", None))
        self.pushButton_5.setText(_translate("MainWindow", "Start ", None))
        self.label_6.setText(_translate("MainWindow", "Reference DNA File", None))
        self.pushButton_4.setText(_translate("MainWindow", "Browse", None))
        self.radioButton.setText(_translate("MainWindow", "Single End", None))
        self.radioButton_2.setText(_translate("MainWindow", "Pair End", None))
        self.radioButton_3.setText(_translate("MainWindow", "Yes", None))
        self.radioButton_4.setText(_translate("MainWindow", "No", None))
        self.pushButton_2.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_7.setText(_translate("MainWindow", "Select Work Folder", None))
        self.label_2.setText(_translate("MainWindow", "Rename Output Files", None))

import resources_rc
