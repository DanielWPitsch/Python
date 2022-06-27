# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:09:35 2022

@author: dpits
"""

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
#eof, split
#soma = factorial(n1)+factorial(n2)

#entrada = input()
t = 0
soma= 0;
while t < 2:
    try:    
        entrada = float(input())
        soma = soma + factorial(entrada)
        t = t+1
    except:
        break;
    
print(soma)