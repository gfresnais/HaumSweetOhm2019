#! /usr/bin/env python

import time

import paho.mqtt.client as mqtt

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


def main():
    client = mqtt.Client()
    client.connect("mpd.lan", 1883)

    client.on_connect = on_connect
    client.on_message = on_message

    return client
