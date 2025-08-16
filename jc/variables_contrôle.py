# import tkinter

# # Création et paramétrage de la fernetre 

# app = tkinter.Tk()
# app.geometry("400x300")
# app.title ("variable tkinter")

# #Widgets .....

# label = tkinter.Label(app,text="Bonjour !)")
# label.pack()

# #Boucle principâle 
 

# app.mainloop()





"""
StringVar() :Chaine de caractéres [str]
IntVar()    :nombre entier [int]
DoubleVar() :nombre flottant [float]
BooleanVar():Booléan [bool]
"""




# import tkinter

# # Création et paramétrage de la fenêtre
# app = tkinter.Tk()
# app.geometry("400x300")
# app.title("Variable tkinter")

# #Widgets .....
# # var_label = tkinter.StringVar()
# # label = tkinter.Label(app,text="",textvariable="var_label")
# # var_label.set("COUCOU")
# # print("label :",var_label.get())
# # label.pack()
# var_label = tkinter.StringVar()
# label = tkinter.Label(app,textvariable=var_label)
# var_label.set("coucou")
# print("label :",var_label.get())
# label.pack()

# #Boucle principâle
# app.mainloop()










# import tkinter

# # Création et paramétrage de la fenêtre
# app = tkinter.Tk()
# app.geometry("400x300")
# app.title("Variable tkinter")

# #Widgets .....
# var_entry = tkinter.StringVar()
# entry = tkinter.Entry(app,textvariable=var_entry)
# var_label = tkinter.StringVar()
# label = tkinter.Label(app,textvariable=var_label)
# var_label.set("coucla label...")

# entry.pack()
# label.pack()

# #Boucle principâle
# app.mainloop()








# import tkinter


# # Observateur 
# def update_label (*args):
#     var_label.set(var_entry.get())

# # Création et paramétrage de la fenêtre
# app = tkinter.Tk()
# app.geometry("400x300")
# app.title("Variable tkinter")

# #Widgets .....
# var_entry = tkinter.StringVar()
# var_entry.trace("w",update_label)
# entry = tkinter.Entry(app,textvariable=var_entry)
# var_label = tkinter.StringVar()
# label = tkinter.Label(app,textvariable=var_label)


# entry.pack()
# label.pack()

# #Boucle principâle
# app.mainloop()









# import tkinter


# # Observateur 
# def update_observer (*args):
#     if var_gender.get():
#         print("C'est un Homme")
#     else:
#         print("C'est une Femme")

# # Création et paramétrage de la fenêtre
# app = tkinter.Tk()
# app.geometry("400x300")
# app.title("Variable tkinter")

# #Widgets .....
# var_gender = tkinter.IntVar()
# var_gender.trace("w",update_observer)
# radio1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
# radio2 = tkinter.Radiobutton(app, text="Femme", value=0, variable=var_gender)
# radio1.pack()
# radio2.pack()
# #Boucle principâle
# app.mainloop()










import tkinter


# Observateur 
def update_observer (*args):
    if var_gender.get():
        var_label_gender.set("C'est un Homme")
    else:
        var_label_gender.set("C'est une Femme")
# Création et paramétrage de la fenêtre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variable tkinter")

#Widgets .....
var_gender = tkinter.IntVar()
var_gender.trace("w",update_observer)
radio1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio2 = tkinter.Radiobutton(app, text="Femme", value=0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label_gender)

radio1.pack()
radio2.pack()
label_gender.pack()
#Boucle principâle 
app.mainloop()
