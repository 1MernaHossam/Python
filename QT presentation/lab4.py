#set geometry 
import sys
from PyQt5.QtWidgets import QApplication,QWidget
#QApplication....application
#QWidget....screen
#QMainWindow...screen
a=QApplication(sys.argv)#connection between qt and python(library sys) to create application
t=QWidget()# make screen
t.setWindowTitle("qt5")#make tittle
t.setGeometry(50,100,300,400)#geometry take 4 parameter ( x co-ordinate, y co-ordinate,Width  ,Height ) in  the screen
t.show()#show screen
sys.exit(a.exec_())
