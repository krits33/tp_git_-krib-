#!/usr/bin/env python

import sys

print(sys.argv)

def add(a,b):
      return a+b
#nombre_d'arg correcte
nombre_darg=len(sys.argv)-1   
if (nombre_darg <2):
             print("Veuillez fournir les 2 valeurs en arguement svp")
             x=int(input("Veuillez inserer la valeur de x:"))
             y=int(input("Veuillez inserer la valeur de y:"))
elif (nombre_darg > 2):
              print("Inserez seulement les 2 valeurs en arguement")
else:
	x=int( sys.argv[1] )
	y=int( sys.argv[2] )

print(add(x,y))
