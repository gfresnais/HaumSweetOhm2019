#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# test_it.py
#
# Copyright © 2019 Mathieu Gaborit (matael) <mathieu@matael.org>
#
# Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
# Mathieu (matael) Gaborit wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a beer or coffee in return
#

from mqttmpd import MQTTMPDController

# instanciating a controller
controller = MQTTMPDController(
    mqtt_broker='localhost',
    mqtt_client_id='mpd_controller',
    mqtt_topicbase='laumio/all',
    mqtt_port=1883,
    mpd_server='localhost',
    mpd_port=6600
)

controller.loop_forever()
