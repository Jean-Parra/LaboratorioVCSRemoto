# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:10:50 2020

@author: Jean Parra
"""

import random
ponderado = {"A":[1, 11], "2":[2], "3":[3], "4":[4], "5":[5], "6":[6], "7":[7], "8":[8], "9":[9], "J":[10], "Q":[10], "K":[10]}

simbolos = ["C", "D", "T", "P"]
cartas = ponderado.keys()
valores = ponderado.values()

cartas2 = ["A", "2", "3", "4"]
cartas3 = ["5", "6", "7", "8"]
cartas4 = ["9", "J", "Q", "K"] 

def combinar(lista1, lista2):
    listaC = list(zip(cartas2, simbolos))    
    listaD = list(zip(cartas3, simbolos))
    listaE = list(zip(cartas4, simbolos))
    listaG = listaC + listaD + listaE
    baraja = dict(zip(listaG, valores)) 
    print("Baraja:",baraja)
    return baraja 

baraja0=combinar(cartas, simbolos)

baraja2 = baraja0.items()

orden = ["A, C=1, 11", "2, D=2", "3, T=3", "4, P=4",
               "5, C=5", "6, D=6", "7, T=7", "8, P=8", 
               "9, C=9", "J, D=10", "Q, T=10", "K, P=10"]

def revolver():
    random.shuffle(orden)
    barajax = {}
    for valor in orden:
        keyValue=valor.split("=")
        barajax[keyValue[0]]=keyValue[1]
    return barajax

print("")
desorden = revolver()
print("la Baraja desordenada es: ", desorden)

cartas_jugador = []
cartas_tallador = []
  