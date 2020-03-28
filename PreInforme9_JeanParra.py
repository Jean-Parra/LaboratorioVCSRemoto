# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:08:08 2020

@author: DORIS GELVEZ
"""

#%%ejercicio 19

x1 = float(input("ingrese el valor de x1: "))
x2 = float(input("ingrese el valor de x2: "))
y1 = float(input("ingrese el valor de y1: "))
y2 = float(input("ingrese el valor de y2: "))
d = print("la distancia euclidiana es: " + str(((x2-x1)**2+(y2-y1)**2)**0.5))



#%%ejercicio 23

n = int(input("ingrese un numero de 4 digitos: "))
c4 = n%10
c3 = (n%100)//10
c2 = (n%1000)//100
c1 = (n-(n%1000)) //1000
print(str(c4) + str(c3) + str(c2) + str(c1))


#%%ejercicio 30

n1 = float(input("ingrse la primera nota: "))
n2 = float(input("ingrese la segunda nota: "))
n3 = float(input("ingrese la tercera nota: "))
n4 = float(input("ingrese la cuarta nota: "))
n5 = float(input("ingrese la quinta nota: "))
p1 = n1 * 0.15
p2 = n2 * 0.20
p3 = n3 * 0.15
p4 = n4 * 0.30
p5 = n5 * 0.20
nt = p1 + p2 + p3 + p4 + p5
if nt<2.0:
    print ("su nota es: " + str(nt))
elif nt<3.0:
	print ("su nota es: " + str(nt) + " reprobo")
elif nt>= 3.0: 
	print ("su nota es: " + str(nt) + " aprobo")
elif nt > 4.5:
	print ("su nota es: " + str(nt) + " felicitaciones")
                  
    
#%%ejercicio 60

n = int(input("ingrese la cantidad de filas: "))
if n > 0:
    for i in range (1, n+1):
        print("")
        for j in range (1, i+1):
            print (j, end=" ")
else:
    print("el numero ingresado es invalivo")      
         
          
              
          
    
