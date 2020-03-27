# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# punto 12

a  =  float ( input ( "ingrese el valor del primer numero: " ))
b  =  float ( input ( "ingrese el valor del segundo numero: " ))
c  =  float ( input ( "ingrese el valor del tercer numero: " ))

d  =  b ** 2  - 4 * a * c
e  =  2 * a 

if  d  >  0 :
    print ( "x1 =" , ( - b  +  d ** 0.5 ) / e )
    print ( "x2 =" , ( - b  -  d ** 0.5 ) / e )

elif  d  ==  0 :
        print ( "x1 = x2 =" , - b / e )

elif  d  <  0 :
         print ( "no exixte solucion de la ecuacion cuadratica en el dominio de los reales" )