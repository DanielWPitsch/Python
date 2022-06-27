# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:18:38 2022

@author: dpits
"""

tamanho = int(input())
matriz = [[],[]]
l = 0
c = 0
while l < tamanho:
    matriz[[l],[c]] = matriz.append("")
    l += 1
    while c < tamanho:
        matriz[[l][c]] = matriz.append("")
        c += 1
print(matriz)