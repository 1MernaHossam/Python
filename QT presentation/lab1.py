#PyQt5 .....PYTHON QT ..... library not in python  that you  make install
#sys ......library in python
#conection qt with python through method.....sys.argv
#conection between sys and application(qt) that i want to make it 
#by method .....sys.argv
#sys.argv from sys

#tkinter vs qt

#tkinter not need that connection(metod to connect) because tkinter library in python
#qt not library in python
#application from qt 


import sys
from PyQt5.QtWidgets import QApplication,QWidget
#QApplication....application
#QWidget....screen
#QMainWindow...screen
a=QApplication(sys.argv)#connection between qt and python(library sys) to create application
root=QWidget()# make screen
root.show()#show screens
#mailoop()..... in tkinter to run project 
#sys.exit(a.exec_())..... in qt to run project 

#what happen if i delete this line(line 25) ?
#ans:the screen appear and disappear at same time
sys.exit(a.exec_())
