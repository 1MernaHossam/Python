#make tittle &resize screen
import sys
from PyQt5.QtWidgets import QApplication,QWidget
#QApplication....application
#QWidget....screen
a=QApplication(sys.argv)#connection between qt and python(library sys) to create application
t=QWidget()# make screen
t.setWindowTitle("qt5")#make tittle
t.resize(200,300)#resize(Width  ,Height) the screen
t.show()#show screen
sys.exit(a.exec_())
