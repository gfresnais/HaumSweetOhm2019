

import tkinter as tk

import sys
import os
import time

from laumio import *


tab=[1,0,0,0,0,0,0,0,0,0,0,0,0,0]



def V1():
    if (L1.get() == 'r') :
        L1.set('g')
        tab[1]='g'
    elif (L1.get() == 'g'):
        L1.set('b')
        tab[1]='b'
    else :
        L1.set('r')
        tab[1]='r'
        
def V2():
    if (L2.get() == 'r') :
        L2.set('g')
        tab[2]='g'
    elif (L2.get() == 'g'):
        L2.set('b')
        tab[2]='b'
    else :
        L2.set('r')
        tab[2]='r'

def V3():
    if (L3.get() == 'r') :
        L3.set('g')
        tab[3]='g'
    elif (L3.get() == 'g'):
        L3.set('b')
        tab[3]='b'
    else :
        L3.set('r')
        tab[3]='r'

def V4():
    if (L4.get() == 'r') :
        L4.set('g')
        tab[4]='g'
    elif (L4.get() == 'g'):
        L4.set('b')
        tab[4]='b'
    else :
        L4.set('r')
        tab[4]='r'

def V5():
    if (L5.get() == 'r') :
        L5.set('g')
        tab[5]='g'
    elif (L5.get() == 'g'):
        L5.set('b')
        tab[5]='b'
    else :
        L5.set('r')
        tab[5]='r'

def V6():
    if (L6.get() == 'r') :
        L6.set('g')
        tab[6]='g'
    elif (L6.get() == 'g'):
        L6.set('b')
        tab[6]='b'
    else :
        L6.set('r')
        tab[6]='r'

def V7():
    if (L7.get() == 'r') :
        L7.set('g')
        tab[7]='g'
    elif (L7.get() == 'g'):
        L7.set('b')
        tab[7]='b'
    else :
        L7.set('r')
        tab[7]='r'

def V8():
    if (L8.get() == 'r') :
        L8.set('g')
        tab[8]='g'
    elif (L8.get() == 'g'):
        L8.set('b')
        tab[8]='b'
    else :
        L8.set('r')
        tab[8]='r'

def V9():
    if (L9.get() == 'r') :
        L9.set('g')
        tab[9]='g'
    elif (L9.get() == 'g'):
        L9.set('b')
        tab[9]='b'
    else :
        L9.set('r')
        tab[9]='r'


def V10():
    if (L10.get() == 'r') :
        L10.set('g')
        tab[10]='g'
    elif (L10.get() == 'g'):
        L10.set('b')
        tab[10]='b'
    else :
        L10.set('r')
        tab[10]='r'

def V11():
    if (L11.get() == 'r') :
        L11.set('g')
        tab[11]='g'
    elif (L11.get() == 'g'):
        L11.set('b')
        tab[11]='b'
    else :
        L11.set('r')
        tab[11]='r'

def V12():
    if (L12.get() == 'r') :
        L12.set('g')
        tab[12]='g'
    elif (L12.get() == 'g'):
        L12.set('b')
        tab[12]='b'
    else :
        L12.set('r')
        tab[12]='r'

def V13():
    if (L13.get() == 'r') :
        L13.set('g')
        tab[13]='g'
    elif (L13.get() == 'g'):
        L13.set('b')
        tab[13]='b'
    else :
        L13.set('r')
        tab[13]='r'

ip = "192.169.0.181"
l = Laumio(ip)



def fin():
    
    
    for i in range(0, 13):
        j = i+1
        if (tab[j]=='r'):
            r,g,b = 255,0,0
        elif (tab[j]=='g'):
            r,g,b=0,255,0
        elif (tab[j]=='b'):
            r,g,b=0,0,255
        else :
            r,g,b = 0,0,0
        
        
        l.setPixelColor(i, r, g, b)
        time.sleep(0.5)
        
    l.wipeOut()
        
    fenetre.destroy()
        
    

fenetre = tk.Tk()

L1 = tk.StringVar()
L2 = tk.StringVar()
L3 = tk.StringVar()
L4 = tk.StringVar()
L5 = tk.StringVar()
L6 = tk.StringVar()
L7 = tk.StringVar()
L8 = tk.StringVar()
L9 = tk.StringVar()
L10 = tk.StringVar()
L11 = tk.StringVar()
L12 = tk.StringVar()
L13 = tk.StringVar()


while(1):
    
    tk.Button(fenetre, textvariable=L1, command=V1,borderwidth=1).grid(row=1, column=2)
    tk.Button(fenetre, textvariable=L2, command=V2,borderwidth=1).grid(row=2, column=1)
    tk.Button(fenetre, textvariable=L3, command=V3,borderwidth=1).grid(row=2, column=2)
    tk.Button(fenetre, textvariable=L4, command=V4,borderwidth=1).grid(row=2, column=3)
    tk.Button(fenetre, textvariable=L5, command=V5,borderwidth=1).grid(row=2, column=4)
    tk.Button(fenetre, textvariable=L6, command=V6,borderwidth=1).grid(row=3, column=1)
    tk.Button(fenetre, textvariable=L7, command=V7,borderwidth=1).grid(row=3, column=2)
    tk.Button(fenetre, textvariable=L8, command=V8,borderwidth=1).grid(row=3, column=3)
    tk.Button(fenetre, textvariable=L9, command=V9,borderwidth=1).grid(row=3, column=4)
    tk.Button(fenetre, textvariable=L10, command=V10,borderwidth=1).grid(row=4, column=1)
    tk.Button(fenetre, textvariable=L11, command=V11,borderwidth=1).grid(row=4, column=2)
    tk.Button(fenetre, textvariable=L12, command=V12,borderwidth=1).grid(row=4, column=3)
    tk.Button(fenetre, textvariable=L13, command=V13,borderwidth=1).grid(row=4, column=4)

    tk.Button(fenetre, text="finaliser", command=fin,borderwidth=1).grid(row=8, column=7)

    fenetre.mainloop()