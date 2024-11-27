import customtkinter

COUNTER=0

def onClickButton():
	global COUNTER
	COUNTER += 1
	label.configure(text='Compteur : ' + str(COUNTER))
	progressbar.set(COUNTER/100)
	
app = customtkinter.CTk()
app.title("Mon appli")
app.geometry("400x150")

label = customtkinter.CTkLabel(app, text='Compteur : 0')
label.grid(row=0, column=0, pady=(30, 10))

progressbar = customtkinter.CTkProgressBar(app, orientation='horizontal')
progressbar.set(0)
progressbar.grid(row=1, column=0, pady=(10, 10))

button = customtkinter.CTkButton(app, text='Appuyer ici !', command=onClickButton)
button.grid(row=2, column=0, pady=(10, 10))

app.grid_columnconfigure(0, weight=1)

app.mainloop()

