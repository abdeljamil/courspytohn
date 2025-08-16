# import tkinter

# app = tkinter.Tk()
# check_widget = tkinter.Checkbutton(app,text="Publier?",offvalue=2,onvalue=5)
# radio_widget = tkinter.Radiobutton(app,text="Homme",value=1)
# radio_widget1 = tkinter.Radiobutton(app,text="Femme",value=0)
# check_widget.pack()
# radio_widget.pack()
# radio_widget1.pack()
# app.mainloop()



# import tkinter

# app = tkinter.Tk()
# scale_w = tkinter.Scale(app,from_=10,to=100,tickinterval=25)
# spin_w = tkinter.Spinbox(app,from_=1,to=10)
# scale_w.pack()
# spin_w.pack()
# app.mainloop()



# import tkinter

# app = tkinter.Tk()
# ib = tkinter.Listbox(app)
# ib.insert(1,"Windows")
# ib.insert(2,"GNU/linux")
# ib.insert(3,"MacOS")
# ib.pack()
# app.mainloop()



import tkinter
from tkinter import messagebox

"""
NOTES
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
"""

def show_modal_windows():
    messagebox.showerror("ERREUR","Un problème est survenu ! ")

app = tkinter.Tk()
btn = tkinter.Button(app,text="Déclencher une erreur",command=show_modal_windows)
btn.pack()
app.mainloop()