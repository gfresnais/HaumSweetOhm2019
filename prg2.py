#! /usr/bin/env python

import tkinter as tk

import time

from laumio import *

import paho.mqtt.client as mqtt

import fonctions

tab=[1,0,0,0,0,0,0,0,0,0,0,0,0,0]
ip=[]
ips = fonctions.ips

# Abonnement aux capteurs des boutons poussoirs
def subBP(client):
    client.subscribe('capteur_bp/status')
    client.subscribe('capteur_bp/switch/#')
    client.subscribe('capteur_bp/binary_sensor/#')

# Abonnement Télécommande
def subTel(client):
    client.subscribe('remote/+/state')

# Abonnement Présence
def subPres(client):
    client.subscribe('presence/status')

# Abonnement Distance
def subDist(client):
    client.subscribe('distance/status')

# Abonnement Atmosphère
def subAtmo(client):
    client.subscribe('atmosphere/status')

# This is the Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    subBP(client)
    subTel(client)
    #subPres(client)
    #subDist(client)
    #subAtmo(client)

def on_message(client, userdata, msg):
    # Gestion LED BP
    text = 'capteur_bp/switch/'
    if (msg.topic == text + 'led1/state') & (msg.payload.decode() == 'ON'):
        print('Rouge ON')
    elif (msg.topic == text + 'led2/state') & (msg.payload.decode() == 'ON'):
        print('Bleu ON')
    elif (msg.topic == text + 'led3/state') & (msg.payload.decode() == 'ON'):
        print('Orange ON')
    elif (msg.topic == text + 'led4/state') & (msg.payload.decode() == 'ON'):
        print('Vert ON')

    # Gestion BP PRESSED
    text = 'capteur_bp/binary_sensor/'
    if (msg.topic == text + 'bp1/state') & (msg.payload.decode() == 'ON'):
        print('Rouge PRESSED')
    elif (msg.topic == text + 'bp2/state') & (msg.payload.decode() == 'ON'):
        print('Bleu PRESSED')
    elif (msg.topic == text + 'bp3/state') & (msg.payload.decode() == 'ON'):
        print('Orange PRESSED')
    elif (msg.topic == text + 'bp4/state') & (msg.payload.decode() == 'ON'):
        print('Vert PRESSED')

    # Gestion TEL
    text = 'remote/'
    if (msg.topic == text + 'power/state') & (msg.payload.decode() == 'ON'):
        print('Power PRESSED')
    elif (msg.topic == text + 'mode/state') & (msg.payload.decode() == 'ON'):
        print('Mode PRESSED')
    elif (msg.topic == text + 'mute/state') & (msg.payload.decode() == 'ON'):
        print('Mute PRESSED')
    elif (msg.topic == text + 'playp/state') & (msg.payload.decode() == 'ON'):
        print('PlayP PRESSED')
    elif (msg.topic == text + 'prev/state') & (msg.payload.decode() == 'ON'):
        print('Prev PRESSED')
    elif (msg.topic == text + 'next/state') & (msg.payload.decode() == 'ON'):
        print('Next PRESSED')
    elif (msg.topic == text + 'eq/state') & (msg.payload.decode() == 'ON'):
        print('EQ PRESSED')
    elif (msg.topic == text + 'minus/state') & (msg.payload.decode() == 'ON'):
        print('Minus PRESSED')
    elif (msg.topic == text + 'plus/state') & (msg.payload.decode() == 'ON'):
        print('Plus PRESSED')
    elif (msg.topic == text + '0/state') & (msg.payload.decode() == 'ON'):
        print('0 PRESSED')
    elif (msg.topic == text + 'chg/state') & (msg.payload.decode() == 'ON'):
        print('CHG PRESSED')
    elif (msg.topic == text + 'u_sd/state') & (msg.payload.decode() == 'ON'):
        print('U_SD PRESSED')
    elif (msg.topic == text + '1/state') & (msg.payload.decode() == 'ON'):
        print('1 PRESSED')
    elif (msg.topic == text + '2/state') & (msg.payload.decode() == 'ON'):
        print('2 PRESSED')
    elif (msg.topic == text + '3/state') & (msg.payload.decode() == 'ON'):
        print('3 PRESSED')
    elif (msg.topic == text + '4/state') & (msg.payload.decode() == 'ON'):
        print('4 PRESSED')
    elif (msg.topic == text + '5/state') & (msg.payload.decode() == 'ON'):
        print('5 PRESSED')
    elif (msg.topic == text + '6/state') & (msg.payload.decode() == 'ON'):
        print('6 PRESSED')
    elif (msg.topic == text + '7/state') & (msg.payload.decode() == 'ON'):
        print('7 PRESSED')
    elif (msg.topic == text + '8/state') & (msg.payload.decode() == 'ON'):
        print('8 PRESSED')
    elif (msg.topic == text + '9/state') & (msg.payload.decode() == 'ON'):
        print('9 PRESSED')

def V1():
    if (L1.get() == 'r') :
        L1.set('g')
        tab[10]='g'
    elif (L1.get() == 'g'):
        L1.set('b')
        tab[10]='b'
    else :
        L1.set('r')
        tab[10]='r'
        
def V2():
    if (L2.get() == 'r') :
        L2.set('g')
        tab[3]='g'
    elif (L2.get() == 'g'):
        L2.set('b')
        tab[3]='b'
    else :
        L2.set('r')
        tab[3]='r'

def V3():
    if (L3.get() == 'r') :
        L3.set('g')
        tab[9]='g'
    elif (L3.get() == 'g'):
        L3.set('b')
        tab[9]='b'
    else :
        L3.set('r')
        tab[9]='r'

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
        tab[11]='g'
    elif (L5.get() == 'g'):
        L5.set('b')
        tab[11]='b'
    else :
        L5.set('r')
        tab[11]='r'

def V6():
    if (L6.get() == 'r') :
        L6.set('g')
        tab[2]='g'
    elif (L6.get() == 'g'):
        L6.set('b')
        tab[2]='b'
    else :
        L6.set('r')
        tab[2]='r'

def V7():
    if (L7.get() == 'r') :
        L7.set('g')
        tab[8]='g'
    elif (L7.get() == 'g'):
        L7.set('b')
        tab[8]='b'
    else :
        L7.set('r')
        tab[8]='r'

def V8():
    if (L8.get() == 'r') :
        L8.set('g')
        tab[5]='g'
    elif (L8.get() == 'g'):
        L8.set('b')
        tab[5]='b'
    else :
        L8.set('r')
        tab[5]='r'

def V9():
    if (L9.get() == 'r') :
        L9.set('g')
        tab[12]='g'
    elif (L9.get() == 'g'):
        L9.set('b')
        tab[12]='b'
    else :
        L9.set('r')
        tab[12]='r'


def V10():
    if (L10.get() == 'r') :
        L10.set('g')
        tab[1]='g'
    elif (L10.get() == 'g'):
        L10.set('b')
        tab[1]='b'
    else :
        L10.set('r')
        tab[1]='r'

def V11():
    if (L11.get() == 'r') :
        L11.set('g')
        tab[7]='g'
    elif (L11.get() == 'g'):
        L11.set('b')
        tab[7]='b'
    else :
        L11.set('r')
        tab[7]='r'

def V12():
    if (L12.get() == 'r') :
        L12.set('g')
        tab[6]='g'
    elif (L12.get() == 'g'):
        L12.set('b')
        tab[6]='b'
    else :
        L12.set('r')
        tab[6]='r'

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
        
def B1():
    ip.append(ips[0])
    
def B2():
    ip.append(ips[1])
    
def B3():
    ip.append(ips[2])
    
def B4():
    ip.append(ips[3])
    
def B5():
    ip.append(ips[4])
    
def B6():
    ip.append(ips[5])
    
def B7():
    ip.append(ips[6])
    
def B8():
    ip.append(ips[7])
    
def B9():
   ip.append(ips[8])
    
def B10():
    ip.append(ips[9])
    
def B11():
    ip.append(ips[10])


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
        
        
        for k in ip:
            l = Laumio(k)
            l.setPixelColor(i, r, g, b)
            time.sleep(0.1)

    for k in ip:
        l = Laumio(k)
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
    
tk.Button(fenetre, textvariable=L1, command=V1, borderwidth=1).grid(row=1, column=2)
tk.Button(fenetre, textvariable=L2, command=V2, borderwidth=1).grid(row=2, column=1)
tk.Button(fenetre, textvariable=L3, command=V3, borderwidth=1).grid(row=2, column=2)
tk.Button(fenetre, textvariable=L4, command=V4, borderwidth=1).grid(row=2, column=3)
tk.Button(fenetre, textvariable=L5, command=V5, borderwidth=1).grid(row=2, column=4)
tk.Button(fenetre, textvariable=L6, command=V6, borderwidth=1).grid(row=3, column=1)
tk.Button(fenetre, textvariable=L7, command=V7, borderwidth=1).grid(row=3, column=2)
tk.Button(fenetre, textvariable=L8, command=V8, borderwidth=1).grid(row=3, column=3)
tk.Button(fenetre, textvariable=L9, command=V9, borderwidth=1).grid(row=3, column=4)
tk.Button(fenetre, textvariable=L10, command=V10, borderwidth=1).grid(row=4, column=1)
tk.Button(fenetre, textvariable=L11, command=V11, borderwidth=1).grid(row=4, column=2)
tk.Button(fenetre, textvariable=L12, command=V12, borderwidth=1).grid(row=4, column=3)
tk.Button(fenetre, textvariable=L13, command=V13, borderwidth=1).grid(row=4, column=4)
    
tk.Button(fenetre, text='1', command=B1, borderwidth=1).grid(row=6, column=1)
tk.Button(fenetre, text='2', command=B2, borderwidth=1).grid(row=6, column=2)
tk.Button(fenetre, text='3', command=B3, borderwidth=1).grid(row=6, column=3)
tk.Button(fenetre, text='4', command=B4, borderwidth=1).grid(row=6, column=4)
tk.Button(fenetre, text='5', command=B5, borderwidth=1).grid(row=6, column=5)
tk.Button(fenetre, text='6', command=B6, borderwidth=1).grid(row=6, column=6)
tk.Button(fenetre, text='7', command=B7, borderwidth=1).grid(row=7, column=1)
tk.Button(fenetre, text='8', command=B8, borderwidth=1).grid(row=7, column=2)
tk.Button(fenetre, text='9', command=B9, borderwidth=1).grid(row=7, column=3)
tk.Button(fenetre, text='10', command=B10, borderwidth=1).grid(row=7, column=4)
tk.Button(fenetre, text='11', command=B11, borderwidth=1).grid(row=7, column=5)
    
tk.Button(fenetre, text='script1', command=fonctions.script1, borderwidth=1).grid(row=9, column=4)
tk.Button(fenetre, text='script2', command=fonctions.script2, borderwidth=1).grid(row=9, column=5)
    
tk.Button(fenetre, text='red', command=fonctions.red, borderwidth=1).grid(row=10, column=2)
tk.Button(fenetre, text='green', command=fonctions.green, borderwidth=1).grid(row=10, column=3)
tk.Button(fenetre, text='blue', command=fonctions.blue, borderwidth=1).grid(row=10, column=4)
tk.Button(fenetre, text='orange', command=fonctions.orange, borderwidth=1).grid(row=10, column=5)

tk.Label(fenetre, text='', borderwidth=1).grid(row=2, column=6)
    
tk.Button(fenetre, text="finaliser", command=fin, borderwidth=1).grid(row=8, column=7)

#client = mqtt.Client()
#client.connect("mpd.lan", 1883)

#client.on_connect = on_connect
#client.on_message = on_message

#client.loop_start()

fenetre.mainloop()

#client.loop_stop()

#client.disconnect()
