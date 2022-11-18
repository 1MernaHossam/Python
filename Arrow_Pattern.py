import os 
import time
rows = int(input("How many rows of symbol do you want: "))
#rows=7
symbol= input("which symbol do you want to use: ")
#for o in range(15):
#	print(""+"\t", end='\t')
for i in range(10):
	print("\t", end='\t')
for i in range(rows *2):
	if i < rows :
		print((rows-i) * " " + (2*i-1) * symbol)
	elif i >= rows :
		print( (int((2*rows-2)/2)) * " " + 1* symbol)
time.sleep(5)
os.system("cls")
for i in range(300):
	print("\t", end='\t')
for i in range(rows *2):
	if i < rows :
		print(rows * 2 * " " + i * symbol)
	elif i > rows :
		print(rows * 2 * " " + (rows* 2-i) * symbol)
	else:
		print(rows* 3 * symbol)
time.sleep(5)
os.system("cls")
for i in range(rows *2):
	if i < rows :
		print((rows-i) * " " + i * symbol)
	elif i > rows :
		print((i-rows) * " " + (rows* 2-i) * symbol)
	else:
		print(rows* 3 * symbol) 
time.sleep(5)
os.system("cls")

for i in range(rows *2):
	if i > rows :
	    print((i-rows) * " " + ((4*(rows))-(2*i)-1)* symbol)
	elif i <= rows :
		print( (int((2*rows-2)/2)) * " " + 1* symbol)
time.sleep(5)
os.system("cls")


