# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:51:08 2016

@author: DEEPN
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import subprocess
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
        self.pushButton_5.clicked.connect(self.tophat)
        self.textEdit.setReadOnly
        self.textEdit_1.setReadOnly
        self.textEdit_2.setReadOnly
        
        
    def single_end(self):
        self.label_5.hide()
        self.pushButton_2.hide()
        self.textEdit_2.hide()
        self.label_4.setText("R Files")  
        
    def pair_end(self):
         self.label_5.show()
         self.pushButton_2.show()
         self.textEdit_2.show()
         self.label_4.setText("R1 Files")
         
    def annotation(self):
        self.label_7.show()
        self.pushButton_4.show()
        self.textEdit_3.show()
         
    def no_annotation(self):
         self.label_7.hide()
         self.pushButton_4.hide()
         self.textEdit_3.hide()
        
    def browse_file(self):
        #files handling
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        f_1=QFileDialog.getOpenFileNames(None, caption, directory, filter_mask)
        self.textEdit.setText(str(f_1))
        
        
    def browse_file2(self):
        #files handling
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        f_2=QFileDialog.getOpenFileNames(None, caption, directory, filter_mask)
        self.textEdit_2.setText(str(f_2))
        
        
    def browse_file3(self):
       #files handling
        caption="Open File"
        directory='./'
        filter_mask="(*.gtf)"
        f_3=QFileDialog.getOpenFileNames(None, caption, directory, filter_mask)
        self.textEdit_3.setText(str(f_3))
        
   # def tophat(self,files):
        
    #    for path in files:
          #subprocess.call('tophat2 -p 3 --b2-very-sensitive -G ', shell=True)  
           #subprocess.call('/LaCie/tophatgui/mm10Genes.gtf -o
          #  $file4 /LaCie/tophatgui/mm10/mm10 $file1 $file2')
    
        
if __name__ == "__main__":#runs the code if called as a main function
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec_())