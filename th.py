# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:51:08 2016

@author: DEEPN
"""
"""
import sip
sip.setapi('QString', 2)
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
    R4=[]
    R5=[]
    R6=[]
    R7=[]
    #command=""
         
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
        self.pushButton_7.clicked.connect(self.select_folder)
        self.pushButton_8.clicked.connect(self.select_folder_2)
        self.textEdit.setReadOnly
        self.textEdit_3.setReadOnly
        self.textEdit_2.setReadOnly
        self.lineEdit_3.setReadOnly
        self.lineEdit.setText("accepted_hits.bm")
        self.lineEdit_2.setText("unmapped.bm")
        self.listWidget.itemClicked.connect(self.selected_item)       
        
        
        
        
    def selected_item(self):
       global R5
       global R4
       global R7
       for p in self.listWidget.selectedItems():
           R5= os.path.join(str(R4),str(p.text()))#R4 from select_folder2
       for file in os.listdir(R5):
          if file.endswith(".rev.1.bt2"):
              R4=file.strip("rev.1.bt2")
       R7=str(R5+"/"+R4)
       
              
              
    def select_folder(self)  :
        folder=str(QtGui.QFileDialog.getExistingDirectory(QtGui.QFileDialog(), "Locate Output Folder",
                                                                    os.path.expanduser("~"),
                                                                    QtGui.QFileDialog.ShowDirsOnly))
                                                            
        self.lineEdit_3.setText(os.path.basename(folder))  
        global R6
        R6=str(folder)
        
        
    def select_folder_2(self)  :
        folder_2=str(QtGui.QFileDialog.getExistingDirectory(QtGui.QFileDialog(), "Locate DNA Reference File Folder",
                                                                    os.path.expanduser("~"),
                                                                   QtGui.QFileDialog.ShowDirsOnly))
        global R4
        R4=folder_2
        
        sub=next(os.walk(folder_2))[1]     
        for p in sub:
           self.listWidget.addItem(p)
        #if self.listWidget.count()>0:
         # self.listWidget.setItemSelected(,True)   
                                                                    
                                                              
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
        command3=str(R3[0])
        command4=str(R7)
        output_folder=R6
        
         #   command.append("")
        #subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G /Volumes/LaCie/tophatgui/mm10/mm10Genes.gtf -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 /Volumes/LaCie/tophatgui/A_R1_.fastq /Volumes/LaCie/tophatgui/A_R2_.fastq', shell=True)
        if command3 is "":
            if command2 is "":
                for x in range(0,len(R1)):
                    command1=str(R1[x])
                    command2=str(R2[x])
                    subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -o '+output_folder+' '+command4+' '+command1, shell=True)
            else:
                for x in range(0,len(R1)):
                  command1=str(R1[x])
                  command2=str(R2[x])
                  print command1
                  print output_folder
                  print command4
                  print command2
                  subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -o '+output_folder+' '+command4+' '+ command1+' '+command2, shell=True)
        elif command2 is "": 
            for x in range(0,len(R1)):
                command1=str(R1[x])
                subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G '+command3+' -o '+output_folder+' '+command4+' '+ command1, shell=True)
        else:  
          for x in range(0,len(R1)):
            command1=str(R1[x])
            command2=str(R2[x])
            subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G '+command3+' -o '+output_folder+' '+command4+' '+ command1+' '+command2, shell=True)
        
if __name__ == "__main__":#runs the code if called as a main function
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec_())