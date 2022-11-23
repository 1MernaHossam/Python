
#create label...means ctreate"text"
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
#QApplication....application
#QWidget....screen
#QMainWindow...screen
#QPushButton.....PushButton
a=QApplication(sys.argv)#connection between qt and python(library sys) to create application
#make function pressed 
def pressed():
	print("hello qt5_pressed button")
t=QWidget()# make screen
t.setWindowTitle("qt5")#make tittle
t.setGeometry(50,100,300,400)#geometry take 4 parameter ( x co-ordinate, y co-ordinate,Width  ,Height ) in  the screen
v=QLabel("user name",t)#make label('text in label',place that appear on it)
v.move(10,50)
t.show()#show screen
sys.exit(a.exec_())
