# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:51:08 2016

@author: DEEPN
"""
import sip
sip.setapi('QString', 2)

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
from shutil import copy2,copytree
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
    R8=[]
    R9=[]
    qs=[]
    #command=""
         
    def __init__(self): #constructor
    
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.radioButton_2.setChecked(1)
        self.radioButton_3.setChecked(1)
        self.radioButton_8.setChecked(1)
        self.radioButton.clicked.connect(self.single_end)
        self.radioButton_2.clicked.connect(self.pair_end)
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2.clicked.connect(self.browse_file2)
        self.pushButton_4.clicked.connect(self.browse_file3)
        self.radioButton_3.clicked.connect(self.annotation)
        self.radioButton_4.clicked.connect(self.no_annotation)
        #self.pushButton_5.clicked.connect(self.tophat, path, f_1)
        self.pushButton_5.clicked.connect(self.start_queue)
        self.pushButton_7.clicked.connect(self.select_folder)
        self.pushButton_3.clicked.connect(self.select_folder_3)
        self.pushButton_8.clicked.connect(self.select_folder_2)
        self.listWidget.itemClicked.connect(self.selected_item)  
        self.pushButton_6.clicked.connect(self.queue_items)
        self.lineEdit_4.setText("sample")
        
        
        
        
    def selected_item(self):
       global R5
       global R4
       global R7
       for p in self.listWidget.selectedItems():
           R5= os.path.join(str(R4),str(p.text()))#R4 from select_folder2
       for file in os.listdir(R5):
          if file.endswith(".rev.1.bt2"):
              R4=file.replace(".rev.1.bt2","")
       R7=str(R5+"/"+R4)
       print R7
              
              
    def select_folder(self)  :
        folder=str(QtGui.QFileDialog.getExistingDirectory(QtGui.QFileDialog(), "Locate Output Folder",
                                                                    os.path.expanduser("~"),
                                                                    QtGui.QFileDialog.ShowDirsOnly))
                                                            
        self.lineEdit_3.setText(os.path.basename(folder))  
        global R6
        R6=str(folder)
       
        
        
    def select_folder_2(self)  :
        self.listWidget.clear()
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
                                                                    
    def select_folder_3(self)  :
        folder=str(QtGui.QFileDialog.getExistingDirectory(QtGui.QFileDialog(), "Locate Working Folder",
                                                                    os.path.expanduser("~"),
                                                                    QtGui.QFileDialog.ShowDirsOnly))
                                                            
        self.lineEdit_6.setText(os.path.basename(folder))  
        global R8
        R8=str(folder)                                                          
    def single_end(self):
        self.label_5.hide()
        self.pushButton_2.hide()
        self.lineEdit_2.hide()
        self.label_4.setText("R Files")  
        global R2
        R2=""
        
    def pair_end(self):
         self.label_5.show()
         self.pushButton_2.show()
         self.lineEdit_2.show()
         self.label_4.setText("R1 Files")
         
    def annotation(self):
        self.label_7.show()
        self.pushButton_4.show()
        self.lineEdit_5.show()
         
    def no_annotation(self):
         self.label_7.hide()
         self.pushButton_4.hide()
         self.lineEdit_5.hide()
         global R3
         R3=""
        
    def browse_file(self):
        #files handling
        
         
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        
        f_1=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))[0]
        self.lineEdit.setText(str(os.path.basename(f_1)))
        global R1
        R1=f_1
        
            #if textEdit.toPlainText
            
        
    def browse_file2(self):
        #files handling
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        f_2=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))[0]
        self.lineEdit_2.setText(str(os.path.basename(f_2)))
        global R2
        R2=f_2
        
        
        
    def browse_file3(self):
       #files handling
        caption="Open File"
        directory='./'
        filter_mask="(*.gtf)"
        f_3=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))[0]
        self.lineEdit_5.setText(str(os.path.basename(f_3)))
        global R3
        R3=f_3 
    #def tophat(self,files):
     #   for path in files:
      #      print f
          #subprocess.call('tophat2 -p 3 --b2-very-sensitive -G /LaCie/tophatgui/mm10Genes.gtf -o
    # $file4 /LaCie/tophatgui/mm10/mm10 $file1 $file2', shell=True)  
        
    
    def queue_items(self):
        #self.textEdit.append(str(self.lineEdit_4.text()))
         
        command1=""
        command2=str(R2)
        command3=str(R3)
        command4=str(R7)
        global qs
        qs=[]
        
        output_folder=R6
        global R9
        R9=[]
        if self.radioButton_8.isChecked():
            R9=str("very-sensitive")
        elif self.radioButton_5.isChecked():
            R9=str("very-fast")
        elif self.radioButton_6.isChecked():
            R9=str("fast")
        else :
            R9=str("sensitive")    
           
        #subprocess.call('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-very-sensitive -G /Volumes/LaCie/tophatgui/mm10/mm10Genes.gtf -o /Volumes/LaCie/tophatgui/tophat /Volumes/LaCie/tophatgui/mm10/mm10 /Volumes/LaCie/tophatgui/A_R1_.fastq /Volumes/LaCie/tophatgui/A_R2_.fastq', shell=True)
        if command3 is "":
            if command2 is "":
                
                    command1=str(R1)
                    command2=str(R2)
                    qs.append('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-'+R9+' -o '+output_folder+' '+command4+' '+command1)
            else:
                
                  command1=str(R1)
                  command2=str(R2)
                  print '/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-'+R9+' -o '+output_folder+' '+command4+' '+ command1+' '+command2
                  
                  qs.append(str('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-'+R9+' -o '+output_folder+' '+command4+' '+ command1+' '+command2))
        elif command2 is "": 
            
                command1=str(R1)
                qs.append(str('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-'+R9+' -G '+command3+' -o '+output_folder+' '+command4+' '+ command1))
        else:  
            
            command1=str(R1)
            command2=str(R2)
            
            qs.append(str('/Volumes/Lacie/Tophat2final/tophat2 -p 3 --b2-'+R9+' -G '+command3+' -o '+output_folder+' '+command4+' '+ command1+' '+command2))
        
        print qs[0]
        self.textEdit.append(str(self.lineEdit_4.text()))
        qs.append(str(self.lineEdit_4.text()))#sample name
        qs.append(R8)#work folder
        """
        for filename in os.listdir(output_folder):
          if filename=="unmapped.bam":
           os.rename(os.path.join(output_folder,filename), os.path.join(output_folder,filename).replace("unmapped",str(self.lineEdit_2.text())))
          if filename=="accepted_hits.bam":
           os.rename(os.path.join(output_folder,filename), os.path.join(output_folder,filename).replace("accepted_hits",str(self.lineEdit.text()))) 
        """
    def start_queue(self):
         for x in range(0,len(qs)-2,3):
             subprocess.call(qs[x], shell=True)
             directory=os.path.join(R8,qs[x+1])
             while True:
                 mydir = directory
                 try:
                     os.makedirs(mydir)
                     break
                 except OSError, e:
                   if e.errno != 17:
                     raise   
        # time.sleep might help here
                     pass
           
             for filename in os.listdir(R6):     #output folder to work folder  
                 if filename=="accepted_hits.bam":
                     src=os.path.join(R6,filename)
                     copy2(src, directory)
                 if filename=="unmapped.bam":
                     src=os.path.join(R6,filename)
                     copy2(src, directory)  
                 if filename=="logs":
                     src=os.path.join(R6,filename)
                     d=os.path.join(directory,"logs")
                     copytree(src, d)
                     
                     
if __name__ == "__main__":#runs the code if called as a main function
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec_())