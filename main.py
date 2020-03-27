# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# empresa de transporte

PesoAcumulado = 0
D = float(input("ingrese la distancia: "))
L = 64000
PP = 4500
PK = 4000
PM = 8000
VN = 1
VI = 2
while PesoAcumulado <= L *0.95 :
    P = float(input("ingrese el peso: "))
    if P > 10:
        PesoAcumulado = PesoAcumulado + P
        if PesoAcumulado <= L:
            if VN == 1:
                ValorDistancia = PK * D
                ValorPeso = PP * P
                ValorTotal = ValorDistancia + ValorPeso
                print("el valor total es: " + str (ValorDistancia + ValorPeso))
                if P > 100 :
                    print("el valor total es: " + str (ValorTotal * 0.85))
            elif VI == 2:
                ValorDistancia = PM * D
                ValorPeso = PP * P
                print("el valor total es: " + str (ValorDistancia + ValorPeso))
                if P >400 and D >8000:
                    print("el valor total es: " + str (ValorTotal * 0.90))
        else:
            print("el paquete supera el limite")
            PesoAcumulado = PesoAcumulado - P
    else: 
        print("peso no aceptable")
    if PesoAcumulado >= L * 0.95 and L <= 355000 :
        print("el peso del avion es: " + str(PesoAcumulado))
