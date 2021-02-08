# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:30:25 2021

@author: ARTURO
"""

#entrada de texto por pantalla
def ejerc1():
    x = input("introduzca una palabra: ")
    with open('output.txt', 'w') as z:
        if (x == x[::-1]):
            z.write("la palabra {} es palindroma.".format(x))
        else:
            z.write("la palabra {} no es palindroma.".format(x))


    
    