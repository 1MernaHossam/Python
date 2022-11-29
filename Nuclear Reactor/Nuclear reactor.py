import tkinter 
import random
from functools import partial
from PIL import Image, ImageTk
from playsound import playsound
import tk_tools


top = tkinter.Tk()
top.geometry("900x900")
top.title(' welcome Nuclear Reactor')
top.configure(bg='khaki')
#def play():
#	playsound('nuclear_alarm.mp3')
def play():
	playsound('bomb.mp3')
def graph_temp():
	top2 = tkinter.Tk()
	top2.geometry("600x300")
	top2.title('temp Nuclear Reactor')
	top2.configure(bg='Spring Green2')
	# g = plt.Figure(plt.Indicator(
    # mode = "gauge+number",
    # value = 270,
    # domain = {'x': [0, 1], 'y': [0, 1]},
    # title = {'text': "Speed"}))
	#g=np.random.normal(20000,25000,5000)
	#plt.hist(g,50)
	# plt.show()
	gauge = tk_tools.Gauge(top2, max_value=100.0,
                       label='temperature',width=500,min_value=-100.0,divisions=10,yellow=20,red=40,yellow_low=10,red_low=30 ,unit='Celsius',bg='Spring Green2')
	gauge.pack()
	value=random.randint(1,100)
	gauge.set_value(value)
	
def  correct ():	
	t=str("true")

	print (t)
	B_1_2  =tkinter.Label(top , text = str(t)  ,bg = "light cyan", bd= "2", fg  = "maroon2", font = "Arial", height = "3", width = "8")
	B_1_2.place(x=200,y=350)
	top.destroy()
	top1 = tkinter.Tk()
	top1.geometry("1500x1500")
	top1.title('Nuclear Reactor')
	top1.configure(bg='snow')
	
		
	label_Temp=tkinter.Label(top1 , text = "123",bg = "light cyan", bd= "2", fg  = "maroon2", font = "Arial", height = "3", width = "8" )
	label_Temp.place(x=500,y=100)
	def random_Temp():
		value=random.randint(1,1000)
		label_Temp.config(text=str(value))
		top1.after(400, random_Temp)
	random_Temp()
	label_Humidity=tkinter.Label(top1 , text = "3.5",bg = "light cyan", bd= "2", fg  = "maroon4", font = "Arial", height = "3", width = "8")
	label_Humidity.place(x=500,y=650)
	def random_Humidity():
		value=random.randint(1,500)
		label_Humidity.config(text=str(value))
		top1.after(200, random_Humidity)
	random_Humidity()
	label_Day=tkinter.Label(top1 , text ="Day",bg = "light cyan", bd= "2", fg  = "maroon3", font = "Arial", height = "3", width = "8")
	label_Day.place(x=500,y=400)
	def random_Day():
		list1 = ['Night', 'MidNight', 'MidDay', 'Morning', 'AfterNoon', 'Evening','Dawn','Dusk']
		value=random.choice(list1)
		label_Day.config(text=str(value))
		top1.after(400, random_Day)
	random_Day()
		# Create an object of tkinter ImageTk
	photo_m=tkinter.PhotoImage(file="Nuclear.png")
	photo_m=photo_m.subsample(1,1)
		# Create a Label Widget to display the text or Image
	label99 =tkinter.Label(top1,image = photo_m)
	label99.place(x=700,y=50)
	Btn_Temp = tkinter.Button(top1, text ="Temperature", bd= "5", bg= "gray17", fg  = "Lightpink1", font = "Arial", height = "6", width = "16",command =graph_temp)
	Btn_Temp.place(x=100,y=50)

	Btn_Day = tkinter.Button(top1, text ="Day", bd= "5", bg = "gray17", fg  = "Lightpink2", font = "Arial", height = "6", width = "16")
	Btn_Day.place(x=100,y=350)

	Btn_Humidity = tkinter.Button(top1, text ="Humidity",bg = "gray17", bd= "2", fg  = "Lightpink3", font = "Arial", height = "6", width = "16")
	Btn_Humidity.place(x=100,y=600)
	top1.after(300,play)
		# b55 = tkinter.Button(top1 , text = "kitty", bd = '9',bg = 'light goldenrod'  )
		# b55.place(x=600,y=450)

def validateLogin(username, password):
	
	username_check=username.get()
	password_check=password.get()

	if username_check=="Merna" and password_check=="881999":
		correct()
	else:
		print("false")
		global i
		i=i+1
		print(i)
		B_1_9  =tkinter.Label(top , text = "Error"  ,bg = "light cyan", bd= "2", fg  = "maroon2", font = "Arial", height = "3", width = "10")
		B_1_9.place(x=100,y=350)

		B_1_1  =tkinter.Label(top , text = str(i)  ,bg = "light cyan", bd= "2", fg  = "maroon2", font = "Arial", height = "3", width = "8")
		B_1_1.place(x=200,y=350)
		if i>=3:
			print("no")	
			top.destroy()
i=0

# def show_list():
	# correct()
	# play()
user_name =tkinter.Label(top,text = "Username").place(x = 40,y = 60)
username =tkinter.StringVar()
user_name_input_area =tkinter.Entry(top, textvariable=username, show='*',width = 30).place(x = 110,y = 60)

user_password =tkinter.Label(top,text = "Password").place(x = 40,y = 100)
password = tkinter.StringVar()
user_password_entry_area =tkinter.Entry(top, textvariable=password, show='*',width = 30).place(x = 110,y = 100)
validateLogin = partial(validateLogin, username, password)

submit_button =tkinter.Button(top,text = "Submit", command=validateLogin).place(x = 150,y = 130)
top.mainloop()
# if __name__ == "__main__":
	# process1 = multiprocessing.Process(target=play)
	# process2 = multiprocessing.Process(target=validateLogin)
	# process1.start()
	# process2.start()