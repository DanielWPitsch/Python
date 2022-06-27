# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:49:43 2022

@author: dpits
"""
teste = True

while teste == True:
    entrada = input()
    Alice,Beto,Clara = entrada.split(' ')
    if Alice != (Beto and Clara):
        print('A')
        teste = False
    if Beto != (Alice and Clara):
        print ('B')
        teste = False
    if Clara != (Beto and Alice):
        print('C')
        teste = False
    if Clara==Beto ==Alice:
        print('*')
