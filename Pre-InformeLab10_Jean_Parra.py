# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:16:40 2020

@author: Jean Parra
"""


#  ------------- Funciones ------------- #
#%%
import numpy as np

def Kellogs():
    Años = np.array([27834,23789,30189,30967,32501,
                     32701,31665,17155,4614,834])
    return Años

def mediapromedio(Años):
    promedio1 = (Años[0] + Años[1])/2
    promedio2 = (Años[8] + Años[9])/2
    print('la diferencia de los promedios de los 2 primeros con los 2 ultimos es de: ' + str(promedio1-promedio2))
#%%
def Menor(Años):
    Pequeño = Años[0]
    long = len(Años)
    for i in range(1,long):
        if Pequeño > float(Años[i]):
            Pequeño = float(Años[i])
    return Pequeño
            
def Mayor(Años):
    Grande = float(Años[0])
    long = len(Años)
    for r in range(1,long):
        if Grande < float(Años[r]):
            Grande = float(Años[r])
    return Grande

#%%
def Orden(Años):
    Ordenanza = np.sort(Años)[::1]
    return Ordenanza


#%%

def median(Años):
    n = len(Años)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(Años)[n//2]
    else:
        return sum(sorted(Años)[n//2-1:n//2+1])/2.0
print('la mediana es: ' + str(median))


 #%%

Años = Kellogs()
mediapromedio(Años)
Pequeño = Menor(Años)
Grande = Mayor(Años)
mediana = median(Años)

print('la diferencia entre el año con mayor y menor utilidad es: ' + str(Grande-Pequeño))
