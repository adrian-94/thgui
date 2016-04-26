# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'th.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
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

class Ui_MainWindow(QtGui.QMainWindow):
     def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
   
        
     def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1920, 985)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Resources/maxresdefault.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 711, 241))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 8, 3, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout.addWidget(self.radioButton_3, 1, 4, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 7, 3, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.radioButton_2, 0, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.radioButton_4 = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout.addWidget(self.radioButton_4, 1, 5, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 6, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 6, 5, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 0, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 5, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.gridLayoutWidget.raise_()
        self.pushButton_6.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

     def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tophat", None))
        self.pushButton_6.setText(_translate("MainWindow", "Abort", None))
        self.radioButton_3.setText(_translate("MainWindow", "Yes", None))
        self.pushButton_5.setText(_translate("MainWindow", "Start ", None))
        self.radioButton_2.setText(_translate("MainWindow", "Pair End", None))
        self.radioButton_4.setText(_translate("MainWindow", "No", None))
        self.pushButton_3.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_4.setText(_translate("MainWindow", "Browse", None))
        self.radioButton.setText(_translate("MainWindow", "Single End", None))
        self.pushButton_2.setText(_translate("MainWindow", "Browse", None))
        self.label_7.setText(_translate("MainWindow", "Annotation File", None))
        self.label_5.setText(_translate("MainWindow", "R2 Files", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))
        self.label_4.setText(_translate("MainWindow", "R1 Files", None))
        self.label_6.setText(_translate("MainWindow", "Reference DNA File", None))
        self.label_3.setText(_translate("MainWindow", "Do you want to use annotation file?", None))
        self.radioButton.clicked.connect(self.single_end)
        
     def single_end(self):
        print("SIngle End")
        
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex=Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
    