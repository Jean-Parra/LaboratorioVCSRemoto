# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:08:34 2020

@author: Jean Parra
"""

lista = [110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73
         ,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51
         ,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91
         ,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35
         ,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]

#la organizacion de la lista

for recorrido in range(1,len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion+1]:
            temp = lista[posicion]
            lista[posicion] = lista[posicion+1]
            lista[posicion+1] = temp
            
print(lista)
print("")
#la diferencia entre el mayor y menor dato de la lista
print('la diferencia entre el numero mayor y el menor es: ',lista[-1]-lista[0])
print("")

#la mediana de la lista 

n = len(lista)
n2 = n/2
if n%2==0:
	mediana = (lista[25] + lista[26]) / 2
else:
	mediana = lista[n2+1]
    
print('la mediana es: ',mediana)
print("")

#la media de la lista
cont = 0
for elemento in lista:
    cont += elemento
    media = cont / float(len(lista))

print('la media es: ',media)

print("")
#la diferencia de la lista de mediana y media
print('la diferencia entre la mediana y la media es: ',media-mediana)
print("")

#Semanas por encima y por debajo del promedio

lista1 = [] 
lista2 = [] 
for i in lista:
    if i > media:
        posicion = lista.index(i)
        lista1.append(posicion+1)
    else:
        posicion = lista.index(i)
        lista2.append(posicion+1)


lista1 = lista[28:51]
lista2 = lista[0:27]

print("Las presiones con datos mayores al promedio fue: ",lista1)
print("")
print("las presiones con datos menor al promedio fue: ",lista2)
print("")

#presion promedio

promedio_presion = []
for j in lista:
    j = j *0.00986923
    t = (j*510) / (17.16*0.08206)
    promedio_presion.append(t)
    
suma1 = sum(promedio_presion)
promedio = suma1 /(len(promedio_presion))
print("las temperaturas promedio son: ",promedio)
print("")

#Desviacion estandar
import statistics
Desviacion_estandar = statistics.stdev(promedio_presion)
print("La desviacion estandar es: ",Desviacion_estandar)
print("")

#Semanas por encima y por debajo del promedio de la temperatura
listamayor = [] 
listamenor = [] 
for i in promedio_presion:
    if i > promedio:
        posicion = promedio_presion.index(i)
        listamayor.append(posicion)
    else:
        posicion = promedio_presion.index(i)
        listamenor.append(posicion)

listamayor = promedio_presion[28:51]
listamenor = promedio_presion[0:27]

print("Las temperaturas con datos mayores al promedio fue: ",listamayor)
print("")
print("las temperaturas con datos menor al promedio fue: ",listamenor)
print("")


#Desviacion estandar

import statistics
Desviacion_estandar2 = statistics.stdev(listamenor)
print("La desviacion de los datos menores al promedio fue: ",Desviacion_estandar2)
print("")
Desviacion_estandar3 = statistics.stdev(listamayor)
print("La desviacion de los datos mayores al promedio fue: ",Desviacion_estandar2)
print("")
#Media de la desviacion
promedio_desviaciones = (Desviacion_estandar2 + Desviacion_estandar3)/2
print("la media de las desviaciones es: ",promedio_desviaciones)