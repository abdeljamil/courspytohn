#coding:utf-8

import tkinter
#from tkinter import*


# mainapp = tkinter.Tk()
# mainapp.mainloop()
# mainapp.quit()


# mainapp = tkinter.Tk()
# mainapp.title("Mon premier programme fenêtré")
# mainapp.mainloop()


# mainapp = tkinter.Tk()
# mainapp.title("Mon premier programme fenêtré")
# mainapp.minsize(640,480)
# #mainapp.geometry("800*600")
# mainapp.mainloop()


# mainapp = tkinter.Tk()
# mainapp.title("Mon premier programme fenêtré")
# mainapp.maxsize(1280,720)
# #mainapp.geometry("800*600")
# mainapp.mainloop()

# mainapp = tkinter.Tk()
# mainapp.title("Mon premier programme fenêtré")
# #mainapp.maxsize(1280,720)
# #mainapp.geometry("800*600")
# mainapp.resizable(width=False,height=True)
# mainapp.mainloop()

# mainapp = tkinter.Tk()
# mainapp.title("Mon premier programme fenêtré")
# #mainapp.maxsize(1280,720)
# #mainapp.geometry("800*600")
# #mainapp.resizable(width=False,height=True)
# # mainapp.positionfrom("user")
# mainapp.sizefrom("user")
# mainapp.mainloop()


# mainapp = tkinter.Tk()
# mainapp.title("Mon premier programme fenêtré")
#mainapp.maxsize(1280,720)
#mainapp.geometry("800*600")
#mainapp.resizable(width=False,height=True)
# mainapp.positionfrom("user")
#mainapp.sizefrom("user")
# mainapp.geometry("800*600+50+100")
# mainapp.mainloop()


mainapp = tkinter.Tk()
mainapp.title("Mon premier programme fenêtré")

screen_x = int (mainapp.winfo_screenwidth())
screen_y = int (mainapp.winfo_screenheight())
window_x = 800
window_y = 600

postX = (screen_x // 2) - (window_x // 2)
posty = (screen_y // 2) - (window_y // 2)

geo = "{}*{}+{}+{}".format(window_x,window_y,postX,posty)
mainapp.geometry(geo)
mainapp.mainloop()
"""
position_X = (largeur_ecran // 2) - (largeur_fenetre // 2)
position_Y = (hauteur_ecran // 2) - (hauteur_fenetre // 2)

"""