#! /usr/bin/env python

import time

import paho.mqtt.client as mqtt


# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    #client.subscribe("laumio/status/#")
    print("Animation rainbow")
    client.publish('laumio/Laumio_OFC168/json', "{'command':'animate_rainbow'}")


def on_message(client, userdata, msg):
    print(msg.payload.decode())


client = mqtt.Client()
client.connect("mpd.lan", 1883)

client.on_connect = on_connect
client.on_message = on_message

print("Start")
client.loop_forever()

client.disconnect()
