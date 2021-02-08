# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:20:39 2021

@author: ARTURO
"""



#asumiendo que solo se puede mover 1 punto por cada paso y en un eje a la vez:
#si el punto es que X > 0 con la menor cantidad de pasos posible
#en X necesitamos movernos minimo 1 paso.
#en Y dependiendo la posicion debe reducirse tal que Y = 0
#por lo tanto K = Y + 1 (K= numero de pasos) donde Y es la posicion inicial
#en el eje 'y' y el '+1' es el movimiento hacia la derecha una vez se hace
#Y = 0, por ende estaremos en el punto (0,0) y para que sea el minimo damos el
#valor minimo entero posible, que en este caso seria 1.

def position():
    y = int(input("inserte la posicion inicial en el eje Y:"))
    k = 0
    if(y > 0):
        while True:
            y-= 1
            k+= 1
            if(y == 0):
                k+= 1
                break
    
    elif(y < 0):
        while True:
            y+= 1
            k+= 1
            if(y == 0):
                k+= 1
                break
     
        
    elif(y == 0):
        k+= 1
        
        
    with open('output.txt', 'w') as file:
        file.write("numero de pasos: {}".format(k))
            
        
  