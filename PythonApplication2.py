from tkinter import *
from functools import partial

def validateLogin(first_name, last_name, password, confirm_password):
	print("First name entered :", first_name.get())
	print("First name entered :", last_name.get())
	print("password entered :", password.get())
	print("Confirm password entered :", confirm_password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('500x300')  
tkWindow.title('Tkinter Registration Form - pythonexamples.org')

#First name label and text entry box
first_nameLabel = Label(tkWindow, text="First Name").grid(row=0, column=0)
first_name = StringVar()
first_nameEntry = Entry(tkWindow, textvariable=first_name).grid(row=0, column=1)  

#Last name label and text entry box
last_nameLabel = Label(tkWindow, text="Last Name").grid(row=1, column=0)
last_name = StringVar()
last_nameEntry = Entry(tkWindow, textvariable=last_name).grid(row=1, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)

#Confirm password label and password entry box
confirm_passwordLabel = Label(tkWindow,text="Confirm Password").grid(row=3, column=0)  
confirm_password = StringVar()
confirm_passwordEntry = Entry(tkWindow, textvariable=confirm_password, show='*').grid(row=3, column=1)

validateLogin = partial(validateLogin, first_name, last_name, password, confirm_password)

#login button
loginButton = Button(tkWindow, text="SignUp", command=validateLogin).grid(row=5, column=0)  

tkWindow.mainloop()
