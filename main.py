#!/usr/bin/env python3

# Import des librairies
import sys
import os
import time

sys.path.append(os.path.dirname(sys.argv[0]) + '/../')
from laumio import *


# Fonction print_usage
# Sert à afficher l'utilisation du Laumio
def print_usage():
    print(
        "Usage: " + sys.argv[0] + "\n\
\n\
    example:\n\
        " + sys.argv[0] + "\n\
")
    sys.exit(1)


if len(sys.argv) != 1:
    print(len(sys.argv))
    print_usage()

# L'ip du Laumio
ip = "Mon IP"

# Création du Laumio
l = Laumio(ip)

# Affichage du statut
print(str(l.status().data))
