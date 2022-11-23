from tkinter import *
def ButtonPress():
	print("Positive thinking will let you do everything better than negative thinking will")
window_1=Tk()
window_1.title("hello")
window_1.geometry('500x700')
window_1.configure(bg="linen")
label_1=Label(window_1,text="mrmr")
photo_m=PhotoImage(file="mar.png")
photo_c=PhotoImage(file="mar.png")
curr_datetime = datetime.now()
label = Label( root, textvariable=curr_datetime, relief=RAISED )
label.place(50,50)
mar_cnt=0
def INC_mar():
	mar_cnt=mar_cnt+1
	return mar_cnt
cro_cnt=0
def INC_cro():
	cro_cnt=cro_cnt+1
	return mar_cnt	
B_1  =Button(window_1 , text = " MAR "  ,bd = '5',image=photo_m,background='bisque2')
B_1.place(x=50,y=300)
B_2  =Button(window_1 , text = " CRO " ,bd = '5',image=photo_c,background='bisque2')
B_2.place(x=150,y=300)
B_3  =Button(window_1 , text = " INC_MAR"  ,bd = '5', command = INC_mar,background='bisque2')
B_3.place(x=50,y=300)
B_4  =Button(window_1 , text = " DEC_MAR " ,bd = '5', command = INC_cro,background='bisque2')
B_4.place(x=150,y=300)
B_5  =Button(window_1 , text = " RST " ,bd = '5' , command = ButtonPress,background='bisque2')
B_5.place(x=300,y=450)


window_1.mainloop()
