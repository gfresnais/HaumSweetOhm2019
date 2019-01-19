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

r, g, b = 255, 0, 0

l.fillColor(r, g, b)

# r = 255
# g = 0
# b = 0

# for i in range(0, 13):
#    l.setPixelColor(i, r, g, b)
#    time.sleep(1)
