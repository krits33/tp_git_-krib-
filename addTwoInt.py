#!/usr/bin/env python

import sys

print(sys.argv)

def add(a,b):
      return a+b
#nombre_d'arg correcte
#sinon l'affichage d'un erreur
nombre_d'arg=len(sys.argv)-1
if (nombre_d'arg <2):
             print("Error detected")

x=int( sys.argv[1] )
y=int( sys.argv[2] )

print(add(x,y))
