# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:51:08 2016

@author: DEEPN
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import subprocess
import os
import sys
import th_ui_2



class MainWindow(QtGui.QMainWindow,th_ui_2.Ui_MainWindow):
    
    R1=[]  
    R2=[]
    R3=[]
    command=""
         
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
        #self.pushButton_5.clicked.connect(self.tophat, path, f_1)
        self.pushButton_5.clicked.connect(self.tophat)
        self.textEdit.setReadOnly
        self.textEdit_3.setReadOnly
        self.textEdit_2.setReadOnly
        
        
        
        
    def single_end(self):
        self.label_5.hide()
        self.pushButton_2.hide()
        self.textEdit_2.hide()
        self.label_4.setText("R Files")  
        global R2
        R2=[""]
        
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
         global R3
         R3=[""]
        
    def browse_file(self):
        #files handling
        
         
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        self.textEdit.setText("")
        f_1=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))
        #for st in f_1:
        for p in f_1:
         self.textEdit.append(str(os.path.basename(p)))
        global R1
        R1=f_1
        
            #if textEdit.toPlainText
            
        
    def browse_file2(self):
        #files handling
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        f_2=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))
        for p in f_2:
         self.textEdit_2.append(str(os.path.basename(p)))
         global R2
         R2=f_2
        
        
        
    def browse_file3(self):
       #files handling
        caption="Open File"
        directory='./'
        filter_mask="(*.gtf)"
        f_3=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))
        for p in f_3:
           self.textEdit_3.append(str(os.path.basename(p)))
        global R3
        R3=f_3
        
    #def tophat(self,files):
     #   for path in files:
      #      print f
          #subprocess.call('tophat2 -p 3 --b2-very-sensitive -G /LaCie/tophatgui/mm10Genes.gtf -o
    # $file4 /LaCie/tophatgui/mm10/mm10 $file1 $file2', shell=True)  
    def tophat(self):
        command1=""
        command2=str(R2[0])
        command3=""
        command3=str(R3[0])
         #   command.append("")
        #subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G /Volumes/LaCie/tophatgui/mm10/mm10Genes.gtf -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 /Volumes/LaCie/tophatgui/A_R1_.fastq /Volumes/LaCie/tophatgui/A_R2_.fastq', shell=True)
        if command3 is "":
            if command2 is "":
                for x in range(0,len(R1)):
                    command1=str(R1[x])
                    command2=str(R2[x])
                    subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 '+ command1, shell=True)
            else:
                for x in range(0,len(R1)):
                  command1=str(R1[x])
                  command2=str(R2[x])
                  subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 '+ command1+' '+command2, shell=True)
        elif command2 is "": 
            for x in range(0,len(R1)):
                command1=str(R1[x])
                subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G '+command3+' -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 '+ command1, shell=True)
        else:  
          for x in range(0,len(R1)):
            command1=str(R1[x])
            command2=str(R2[x])
            subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G '+command3+' -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 '+ command1+' '+command2, shell=True)
        
if __name__ == "__main__":#runs the code if called as a main function
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec_())