import random

lista= []

for i in range (0,16, 1):
     print("teste "+str(i+1)+"º i = ", i, end="; ")
     lista.append(random.randrange(100))
    
print("lista= ", lista)
print("maior: ", max(lista))
print("menor: ", min(lista))

delta=36
raiz = (delta**0.5)
print("delta e sua raiz² são respectivamente:", delta, raiz)

numeros=[]
for l in range(2):
    linha=[]
    for c in range (2):
        linha.append(int(input("Digite um numero: ")))
    numeros.append(linha)
print(numeros)
print("maior linha da matriz", max(numeros)) #nao da certo
print("soma dos elementos da matriz", sum(numeros))