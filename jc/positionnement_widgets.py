
# import tkinter

# app = tkinter.Tk()
# app.geometry("640x480")
# app.title("Positionnement widgets")

# #Widgets .....
# mainframe = tkinter.Frame(app,width=300,height=200,borderwidth=1)
# mainframe.pack()

# btn = tkinter.Button(mainframe,text="BIENVENU")
# btn.pack()
# #Boucle principâle 
# app.mainloop()






import tkinter

app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement widgets")

#Widgets .....
mainframe = tkinter.LabelFrame(app,text="Titre",width=300,height=200,borderwidth=1)
mainframe.pack()

btn = tkinter.Button(app,text="BIENVENU")
btn.pack()
#Boucle principâle 
app.mainloop()
