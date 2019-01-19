#!/usr/bin/env python3

# Import des librairies
import sys
import os
import time

sys.path.append(os.path.dirname(sys.argv[0]) + '/../')
from laumio import *

# L'ip du Laumio
ip = "192.168.4.1"

# Création du Laumio
l = Laumio(ip)

# Affichage du statut
print( l.status() )

l.rainbow()

time.sleep(2)

r, g, b = 255, 0, 0

l.fillColor(r, g, b)

time.sleep(2)

l.wipeOut()

time.sleep(1)

r, g, b = 0, 0, 255

for i in range(0, 13):
    l.setPixelColor(i, r, g, b)
    time.sleep(0.5)
