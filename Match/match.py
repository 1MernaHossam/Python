from datetime import datetime
from tkinter import *
def ButtonPress():
	print("Positive thinking will let you do everything better than negative thinking will")
window_1=Tk()
window_1.title("hello")
window_1.geometry('500x700')
#window_1.configure(bg="linen")
label_1=Label(window_1,text="mrmr")
photo_m=PhotoImage(file="mar.png")
photo_m=photo_m.subsample(5,5)
photo_c=PhotoImage(file="cro.png")
photo_c=photo_c.subsample(2,2)
curr_datetime = datetime.now()
label5  =Label(window_1 , text = "current time")
label5.place(x=20,y=160)
label  =Label(window_1 , text = str(curr_datetime))
label.place(x=120,y=160)
mar_cnt=0
def INC_mar():
	global mar_cnt
	mar_cnt=mar_cnt+1
	print(mar_cnt)
	B_1_2  =Label(window_1 ,  text = str(mar_cnt)   ,bd = '5',background='bisque2')
	B_1_2.place(x=20,y=350)
cro_cnt=0
def INC_cro():
	global cro_cnt
	cro_cnt=cro_cnt+1
	B_1_1  =Label(window_1 , text = str(cro_cnt)  ,bd = '5',background='bisque2')
	B_1_1.place(x=200,y=350)

def rst_cro():
	cro_cnt=0
	mar_cnt=0
	B_1_1  =Label(window_1 , text = str(cro_cnt)  ,bd = '5',background='bisque2')
	B_1_1.place(x=20,y=350)
	B_1_2  =Label(window_1 ,  text = str(mar_cnt)   ,bd = '5',background='bisque2')
	B_1_2.place(x=200,y=350)
B_1  =Label(window_1 , text = " MAR "  ,bd = '5',image=photo_m,background='bisque2')
B_1.place(x=20,y=400)
B_2  =Label(window_1 , text = " CRO " ,bd = '5',image=photo_c,background='bisque2')
B_2.place(x=200,y=400)


B_3  =Button(window_1 , text = " INC_CRO"  ,bd = '5', command = INC_mar,background='bisque2')
B_3.place(x=20,y=550)
B_4  =Button(window_1 , text = " INC_MAR " ,bd = '5', command = INC_cro,background='bisque2')
B_4.place(x=200,y=550)
B_5  =Button(window_1 , text = " RST " ,bd = '5' , command = rst_cro,background='bisque2')
B_5.place(x=125,y=650)


window_1.mainloop()
