#! /usr/bin/env python

import tkinter as tk

import sys
import os
import time

from laumio import *

import mqtt

ips=["Laumio_0FC168", "Laumio_10508F", "Laumio_0FBFBF", "Laumio_104A13", "Laumio_104F03", "Laumio_107DA8", "Laumio_10805F", "Laumio_1D9486", "Laumio_88813D", "Laumio_CD0522", "Laumio_D454DB"]

def blue():
    for i in ips:
        l = Laumio(i)
        l.fillColor(0, 0, 255)
def red():
    for i in ips:
        l = Laumio(i)
        l.fillColor(255, 0, 0)
def green():
    for i in ips:
        l = Laumio(i)
        l.fillColor(0, 255, 0)
def orange():
    for i in ips:
        l = Laumio(i)
        l.fillColor(253, 106, 2)


def script1():
    for j in range(0, 500):
        k = j / 500
        val = 255 * k
        r, g, b = 123, int(val), int(val)
        for i in ips:
            l = Laumio(i)
            l.fillColor(r, g, b)


def script2():
    for j in range(0, 510):
        k = j % 255
        k = int(k)
        r, g, b = 200, k, k
        for i in ips:
            l = Laumio(i)
            l.fillColor(r, g, b)
