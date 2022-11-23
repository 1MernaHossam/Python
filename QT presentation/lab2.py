#2 method to make & show screen
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
#QApplication....application
#QWidget.... screen
#QMainWindow... screen
a=QApplication(sys.argv)#connection between qt and python(library sys) to create application
#2 method to make & show screen
root=QWidget()# make screen
root.show()#show screen
root1=QMainWindow()# make screen
root1.show()#show screen
sys.exit(a.exec_())
