
#press pushbutton with 2 ways and show message when press button
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
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
b=QPushButton("click me",t)#make pushbutton('text in button',place that appear on it)
b.move(20,30)#move( x co-ordinate, y co-ordinate) to determine location of button,that take 2 parameter
#2 method  to pressed 
#b.clicked.connect(pressed)=== b.pressed.connect(pressed)
b.clicked.connect(pressed)#connection between button and func(happen when i pressed button ) method clicked.connect(function that  i want to execute)
b.pressed.connect(pressed)
t.setGeometry(50,100,300,400)#geometry take 4 parameter ( x co-ordinate, y co-ordinate,Width  ,Height ) in  the screen
t.show()#show screen
sys.exit(a.exec_())
