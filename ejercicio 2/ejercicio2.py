# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 12:10:31 2021

@author: ARTURO
"""



#constructor del diccionario 
def dict_constructor():
    import json
    ala = 0
    prub_list = []
    
    p = int(input("inserte el numero de pilotos:"))
#lista con cantidad de pilotos    
    num_pil = ["piloto{}".format(eje+1) for eje in range(p)]
    
    for count in range(p):
#creando segunda lista con puntuaciones        
        ala += 1
        input_string = input("inserte las puntuacion de piloto{} separado por espacios: ".format(ala))
        userList = input_string.split()
        converted_list = [int(aja) for aja in userList]
        prub_list.append(converted_list)
        
        zip_list = zip(num_pil, prub_list)
        pil_dictionary = dict(zip_list)
        
        with open('output1.txt', 'w') as file:
            file.write(json.dumps(pil_dictionary))
        
    return pil_dictionary



#calculadora de campeon de la temporada
def champ_calc(x):    
    test_dict = {}
    number2_pilot = 0    
    for rang in range(0,len(x)):
        number2_pilot += 1
        test_dict["piloto{}".format(number2_pilot)] = sum(x["piloto{}".format(number2_pilot)][:])
        maxV = max(test_dict.values())
        Champions = [k for k, v in test_dict.items() if v == maxV]
        
        with open('output2.txt', 'w') as file:
            for tempVar in Champions:
                file.write('%s\n' % tempVar)


    
