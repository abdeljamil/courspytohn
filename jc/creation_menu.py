# import tkinter

# app = tkinter.Tk()
# app.geometry("640x480")
# app.title("Création de Menu")

# #Widgets .....
# mainmenu = tkinter.Menu(app)
# first_menu = tkinter.Menu(mainmenu)
# first_menu.add_command(label="Option1")
# first_menu.add_command(label="Option2")
# first_menu.add_command(label="Option3")

# second_menu = tkinter.Menu(mainmenu)

# second_menu.add_command(label="commande1")
# second_menu.add_command(label="commande2")
# second_menu.add_command(label="commande3")


# mainmenu.add_cascade(label="Premier",menu=first_menu)
# mainmenu.add_cascade(label="Second",menu=second_menu)
# #Boucle principâle 
# app.config(menu=mainmenu)
# app.mainloop()







# import tkinter


# def hello():
#     print("Coucou !!")


# # création de la fenetre + paramétre
# app = tkinter.Tk()
# app.geometry("640x480")
# app.title("Création de Menu")

# #Widgets .....
# mainmenu = tkinter.Menu(app)
# first_menu = tkinter.Menu(mainmenu)
# first_menu.add_command(label="Option1",command=hello)
# first_menu.add_command(label="Option2")
# first_menu.add_command(label="Option3")

# second_menu = tkinter.Menu(mainmenu)

# second_menu.add_command(label="commande1")
# second_menu.add_command(label="commande2")
# second_menu.add_command(label="commande3")


# mainmenu.add_cascade(label="Premier",menu=first_menu)
# mainmenu.add_cascade(label="Second",menu=second_menu)
# #Boucle principâle 
# app.config(menu=mainmenu)
# app.mainloop()






# import tkinter

# # création de la fenetre + paramétre
# app = tkinter.Tk()
# app.geometry("640x480")
# app.title("Création de Menu")

# #Widgets .....
# mainmenu = tkinter.Menu(app)
# first_menu = tkinter.Menu(mainmenu,tearoff=0)
# first_menu.add_command(label="Option1")
# first_menu.add_command(label="Option2")
# first_menu.add_command(label="quitter",command=app.quit)

# second_menu = tkinter.Menu(mainmenu,tearoff=0)

# second_menu.add_command(label="commande1")
# second_menu.add_command(label="commande2")
# second_menu.add_command(label="commande3")


# mainmenu.add_cascade(label="Premier",menu=first_menu)
# mainmenu.add_cascade(label="Second",menu=second_menu)
# #Boucle principâle 
# app.config(menu=mainmenu)
# app.mainloop()









# import tkinter

# # add_checkbuttom()
# # add_radiobutton()
# # add_separator()




# def show_about():
#     about_window = tkinter.Toplevel(app)
#     about_window.title("A propos")
#     ib = tkinter.Label(about_window,text="Bonjour!!")
#     ib.pack()
# # création de la fenetre + paramétre
# app = tkinter.Tk()
# app.geometry("640x480")
# app.title("Création de Menu")

# #Widgets .....
# mainmenu = tkinter.Menu(app)
# first_menu = tkinter.Menu(mainmenu,tearoff=0)
# first_menu.add_command(label="Option1")
# first_menu.add_command(label="Option2")
# first_menu.add_command(label="quitter",command=app.quit)

# second_menu = tkinter.Menu(mainmenu,tearoff=0)

# second_menu.add_command(label="commande0")
# second_menu.add_command(label="commande1")
# second_menu.add_command(label="A propos",command=show_about)


# mainmenu.add_cascade(label="Premier",menu=first_menu)
# mainmenu.add_cascade(label="Second",menu=second_menu)
# #Boucle principâle 
# app.config(menu=mainmenu)
# app.mainloop()










import tkinter

# add_checkbuttom()
# add_radiobutton()
# add_separator()




def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    ib = tkinter.Label(about_window,text="Bonjour!!")
    ib.pack()
# création de la fenetre + paramétre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Création de Menu")

#Widgets .....
mainmenu = tkinter.Menu(app)
first_menu = tkinter.Menu(mainmenu,tearoff=0)
first_menu.add_command(label="Option1")
first_menu.add_separator()
first_menu.add_command(label="Option2")
first_menu.add_command(label="quitter",command=app.quit)

second_menu = tkinter.Menu(mainmenu,tearoff=0)

second_menu.add_command(label="commande0")
second_menu.add_command(label="commande1")
second_menu.add_command(label="A propos",command=show_about)


mainmenu.add_cascade(label="Premier",menu=first_menu)
mainmenu.add_cascade(label="Second",menu=second_menu)
#Boucle principâle 
app.config(menu=mainmenu)
app.mainloop()