while True:
	print("Select Mode.")
	print("Press 1 for Scientific Mode.")
	print("Press 2 for Programmable Mode.")
	Mode=int(input("Enter your choice"))
	if Mode==1:
		num1 = int(input('Enter your first number: '))
		num2 = int (input('Enter your second number: '))
		print("Select Operation")
		print("1.Add")
		print("2.Subtract")
		print("3.Multiply")
		print("4.floor division")
		print("5.integer division")
		print("6.Modulus")
		print("7.exponential")
		choice= input('Enter Operation: ')
		if choice in ('1','2','3','4','5','6','7'):
			if choice=='1':
				print(num1, "+", num2, "=" ,num1+num2)
			elif choice=='2':
				print(num1, "-", num2, "=" ,num1-num2)
			elif choice=='3':
				print(num1, "*", num2 ,"=" ,num1*num2)
			elif choice=='4':
				print(num1, "//", num2, "=" ,num1//num2)
			elif choice=='5':
				print(num1 ,"/", num2, "=" ,num1/num2)
			elif choice=='6':
				print(num1, "%", num2 ,"=" ,num1%num2)
			elif choice=='7':
				print(num1 ,"**", num2 ,"=" ,num1**num2)
			else:
				print("invalid input")
	elif Mode==2:
		num = int(input('Enter your first number: '))
		print("Select Operation")
		print("1.convert decimal to binary")
		print("2.convert binary to decimal")
		print("3.convert decimal to hexa")
		print("4.convert hexa to deciaml")
		print("5.convert decimal to octal")
		print("6.convert octal to decimal")
		choice1= input('Enter Operation: ')
		if choice1 in ('1','2','3','4','5','6'):
			if choice1=='1':
				print(num,"=" ,bin(int(num)))
			elif choice1=='2':
				print(num, "=", int(str(num), 2))
			elif choice1=='3':
				print(num,"=" ,hex(int(num)))
			elif choice1=='4':
				print(num, "=" ,int(str(num), 16))
			elif choice1=='5':
				print(num, "=" ,oct(int(num)))
			elif choice1=='6':
				print(num,"=" ,int(str(num),8))
			else:
				print("invalid input")


