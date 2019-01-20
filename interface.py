from tkinter import *


"""def open_window(laumios):
    fenetre2 = Tk()
    value = StringVar()
    value.set("texte par défaut")
    entree = Entry(fenetre, textvariable=str, width=30)
    entree.pack()"""


"""fenetre = Tk()

menubar = Menu(fenetre)
menu1=Menu(menubar, tearoff=0)
menu1.add_command(label="quitter",command=fenetre.quit)
menubar.add_cascade(label="command", menu=menu1)

fenetre.config(menu=menubar)


Button(fenetre, text="laumios 1", command=open_window(1), borderwidth=2).grid(row=1, column=1)
Button(fenetre, text="laumios 2", command=open_window(2), borderwidth=2).grid(row=1, column=2)
Button(fenetre, text="laumios 3", command=open_window(3), borderwidth=2).grid(row=1, column=3)
Button(fenetre, text="laumios 4", command=open_window(4), borderwidth=2).grid(row=2, column=1)
Button(fenetre, text="laumios 5", command=open_window(5), borderwidth=2).grid(row=2, column=2)
Button(fenetre, text="laumios 6", command=open_window(6), borderwidth=2).grid(row=2, column=3)
Button(fenetre, text="laumios 7", command=open_window(7), borderwidth=2).grid(row=3, column=1)
Button(fenetre, text="laumios 8", command=open_window(8), borderwidth=2).grid(row=3, column=2)
Button(fenetre, text="laumios 9", command=open_window(9), borderwidth=2).grid(row=3, column=3)
Button(fenetre, text="laumios 10", command=open_window(10), borderwidth=2).grid(row=4, column=1)
Button(fenetre, text="laumios 11", command=open_window(11), borderwidth=2).grid(row=4, column=3)
Button(fenetre, text="laumios all", command=open_window(0), borderwidth=2).grid(row=4, column=2)
Button(fenetre, text="quitter", command=fenetre.quit, borderwidth=2).grid(row=5, column=2)

fenetre.mainloop()"""

r=0
g=0
b=0

def recupere():
    r = print(entree.get())

fenetre = Tk()

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()

fenetre.mainloop()

print(r)