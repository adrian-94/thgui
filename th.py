# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:51:08 2016

@author: DEEPN
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import sys
import th_ui_2

class MainWindow(QtGui.QMainWindow,th_ui_2.Ui_MainWindow):
         
    def __init__(self): #constructor
    
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.radioButton_2.setChecked(1)
        self.radioButton_3.setChecked(1)
        self.radioButton.clicked.connect(self.single_end)
        self.radioButton_2.clicked.connect(self.pair_end)
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2.clicked.connect(self.browse_file2)
        self.pushButton_4.clicked.connect(self.browse_file3)
        self.radioButton_3.clicked.connect(self.annotation)
        self.radioButton_4.clicked.connect(self.no_annotation)
        
        
        
    def single_end(self):
        self.label_5.hide();
        self.pushButton_2.hide();
        self.label_4.setText("R Files")  
        
    def pair_end(self):
         self.label_5.show();
         self.pushButton_2.show();
         self.label_4.setText("R1 Files")
         
    def annotation(self):
        self.label_7.show()
        self.pushButton_4.show()
         
    def no_annotation(self):
         self.label_7.hide()
         self.pushButton_4.hide()
        
    def browse_file(self):
        f_1=QFileDialog.getOpenFileName()
        self.textEdit.setText(f_1)
        
    def browse_file2(self):
        f_2=QFileDialog.getOpenFileName()
        self.textEdit_2.setText(f_2)
        
    def browse_file3(self):
        f_3=QFileDialog.getOpenFileName()
        self.textEdit_3.setText(f_3)
        
        
if __name__ == "__main__":#runs the code if called as a main function
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec_())