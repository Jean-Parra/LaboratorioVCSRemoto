# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:48:20 2020

@author: Jean Parra
"""

import collections
import random

cartas =  ["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" , "Bleach" , "Arc", "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney"  ,  "Reynolds"  ,  "Short"  ,  "Stanton"  ,  "Deadman"  , "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" ,"Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , "Stone"  ,  "Cannon"  ,  "Garrison"  ,  "Randall"  ,  "Leon"  ,  "Buck"  , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" , "Whitehead"  ,  "Kirby"  ,  "Park"  ,  "Shannon"  ,  "Vlad"  ,  "Pepin"  , "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon"  ,  "Luke"  ,  "Lindsay"  ,  "Payne"  ,  "Gerbvo"  ,  "Hubbard"  , "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower", "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" , "Saint"  ,  "Graham"  ,  "Hodor"  ,  "Ellison"  ,"Roberts"  ,  "Odom"  , "Mann"]
 
premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]


def imprimir(lista):
    print("la lista es: ",lista) 
    return lista
imprimir(cartas)
print("")
imprimir(premium)
print("")

def generador(listaA, N):
    ListaR = []
    Numeros = []
    cont = 0 
    if N <= len(listaA):
        while cont < N:
            numero = random.randint(0, len(listaA)-1)
            if numero not in Numeros:
                Numeros.append(numero)
                cont+=1
        for i in Numeros:
            ListaR.append(listaA[i])
        print("la nueva lista al azar es: ",ListaR)
        print("")
        return ListaR
    else:
        print("la Cantidad de elementos estan fuera del limite")
        print("")
        return None

player = generador(cartas, 10)

def combinador(listaA, listaB):
    listaR = listaA + listaB
    random.shuffle(listaR)
    print("las posiciones aleatorias del juego son: ", listaR)
    print("")
    return listaR

play = combinador(cartas, premium)

sobre1 = generador(play, 5)
sobre2 = generador(play, 5)
sobre3 = generador(play, 5)

sobre1_2 = sobre1 + sobre2

pack = combinador(sobre1_2, sobre3)

print("el paquete de los sobres es: ", pack)
print("")

def loteria(premium, pack, Jugador):
    otra = []
    solo = []
    cartaP = []
    for q in pack:
        if q not in solo:
            solo.append(q) 
        else:
            if q not in otra:
                otra.append(q)
    print("las Cartas repetidas son: ", otra)
    print("")
    for i in pack:
        for f in premium:
            if i == f:
                cartaP.append(i)
    print("las Cartas premium son: ", cartaP)
    print("")
    return cartaP
    if otra and len(cartaP)<=1:
        numero = random.randint(0, 9)
        if numero == 6:
            print("Felicidades")
            print("")
            for i in Jugador:
                for f in premium:
                    if i == f:
                        cartaP.append(i)
            desigual = [carta for carta in premium if carta not in cartaP]
            numero_1 = random.randint(0, len(desigual)-1)
            if desigual:
                pack.append(desigual[numero_1])
                
bueno = loteria(premium, pack, player)  

Jugador = player + pack  
Jugador = [player.lower () for player in player]       
print("los jugadores son: ", Jugador)
print("")

resultado=collections.Counter(Jugador)
print("La cantidad de veces que sale la carta es: ",resultado)
print("")

acum=0
for carta in Jugador:
    if carta[0]== "a" or carta[0]== "b" or carta[0]== "c" or carta[0]== "d" or carta[0]== "e" or carta[0]== "f" or carta[0]== "g" or carta[0]== "h" or carta[0]== "i" or carta[0]== "j" or carta[0]== "k" or carta[0]== "l" or carta[0]== "m" or carta[0]== "n" or carta[0]== "o" or carta[0]== "p" or carta[0]== "q" or carta[0]== "r" or carta[0]== "s" or carta[0]== "t" or carta[0]== "u" or carta[0]== "v" or carta[0]== "w" or carta[0]== "x" or carta[0]== "y" or carta[0]== "z":
      acum+=1  
print("cartas comienzan con una letra del alfabeto ingles son: ",acum)
print("")

print("La carta con el nombre más largo es", max(Jugador))
print("")
print("La carta con el nombre más corto es:", min(Jugador))
print("")


cont=0
for carta in Jugador:
    if "AIVLIS" or "ANAID" in Jugador:
        if carta[0]== "a" or carta[0]== "b" or carta[0]== "c" or carta[0]== "d" or carta[0]== "e" or carta[0]== "f" or carta[0]== "g" or carta[0]== "h" or carta[0]== "i" or carta[0]== "j" or carta[0]== "k" or carta[0]== "l" or carta[0]== "m" or carta[0]== "n" or carta[0]== "o" or carta[0]== "p" or carta[0]== "q" or carta[0]== "r" or carta[0]== "s" or carta[0]== "t" or carta[0]== "u" or carta[0]== "v" or carta[0]== "w" or carta[0]== "x" or carta[0]== "y" or carta[0]== "z":
            if carta[-1]=="a":
                cont+=1
for carta in Jugador:
    if "LEIRBAG" in Jugador:
        if carta[0]== "a" or carta[0]== "b" or carta[0]== "c" or carta[0]== "d" or carta[0]== "e" or carta[0]== "f" or carta[0]== "g" or carta[0]== "h" or carta[0]== "i" or carta[0]== "j" or carta[0]== "k" or carta[0]== "l" or carta[0]== "m" or carta[0]== "n" or carta[0]== "o" or carta[0]== "p" or carta[0]== "q" or carta[0]== "r" or carta[0]== "s" or carta[0]== "t" or carta[0]== "u" or carta[0]== "v" or carta[0]== "w" or carta[0]== "x" or carta[0]== "y" or carta[0]== "z":
            if carta[-1]=="l":
                cont+=1
for carta in Jugador:
    if "SOLRAC" in Jugador:
        if carta[0]== "a" or carta[0]== "b" or carta[0]== "c" or carta[0]== "d" or carta[0]== "e" or carta[0]== "f" or carta[0]== "g" or carta[0]== "h" or carta[0]== "i" or carta[0]== "j" or carta[0]== "k" or carta[0]== "l" or carta[0]== "m" or carta[0]== "n" or carta[0]== "o" or carta[0]== "p" or carta[0]== "q" or carta[0]== "r" or carta[0]== "s" or carta[0]== "t" or carta[0]== "u" or carta[0]== "v" or carta[0]== "w" or carta[0]== "x" or carta[0]== "y" or carta[0]== "z":
            if carta[-1]=="s":
                cont+=1   
for carta in Jugador:
    if "NAILUJ" in Jugador:
        if carta[0]== "a" or carta[0]== "b" or carta[0]== "c" or carta[0]== "d" or carta[0]== "e" or carta[0]== "f" or carta[0]== "g" or carta[0]== "h" or carta[0]== "i" or carta[0]== "j" or carta[0]== "k" or carta[0]== "l" or carta[0]== "m" or carta[0]== "n" or carta[0]== "o" or carta[0]== "p" or carta[0]== "q" or carta[0]== "r" or carta[0]== "s" or carta[0]== "t" or carta[0]== "u" or carta[0]== "v" or carta[0]== "w" or carta[0]== "x" or carta[0]== "y" or carta[0]== "z":
            if carta[-1]=="n":
                cont+=1                
if cont==0:
    print("no tiene cartas premium")
    print("")
else:
    print("El jugador tiene", cont, "cartas premium")     
    