
#coding:utf-8

"""
<nom_variable> = <nom_widget>(widget_parent>,<params>....)
"""
import tkinter

# app = tkinter.Tk()
# msg = "Bienvenue à tous !!!"
# label_welcome = tkinter.Label(app,text=msg)
# label_welcome.pack()
# app.mainloop() 

# app = tkinter.Tk()
# label_welcome = tkinter.Label(app,text="Bienvenue à tous !!!")
# print(label_welcome.cget("text"))
# label_welcome.pack()
# app.mainloop() 


# app = tkinter.Tk()
# label_welcome = tkinter.Label(app,text="Bienvenue à tous !!!")
# label_welcome.config(text="Nouveau message")
# label_welcome.pack()
# app.mainloop() 


# app = tkinter.Tk()
# message_welcome = tkinter.Message(app,text="Bonjour tout le monde et bienvenue sur la chaine formation video !")

# message_welcome.pack()
# app.mainloop() 

# app = tkinter.Tk()
# label_welcome = tkinter.Label(app,text="Bonjour tout le monde et bienvenue sur la chaine formation video !")

# label_welcome.pack()
# app.mainloop() 


# app = tkinter.Tk()
# entry_name = tkinter.Entry(app)

# entry_name.pack()
# app.mainloop()


# app = tkinter.Tk()
# entry_name = tkinter.Entry(app,width=45)

# entry_name.pack()
# app.mainloop()



# app = tkinter.Tk()
# entry_name = tkinter.Entry(app,show="*")

# entry_name.pack()
# app.mainloop()


# app = tkinter.Tk()
# button_quit = tkinter.Button(app,text="OK",width=25)

# button_quit.pack()
# app.mainloop()

# app = tkinter.Tk()
# button_quit = tkinter.Button(app,text="OK",width=25, height=3)

# button_quit.pack()
# app.mainloop()



def hello():
    print("hello sur le terminal")

app = tkinter.Tk()
button_quit = tkinter.Button(app,text="OK",command=hello)

button_quit.pack()
app.mainloop()