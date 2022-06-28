# O vendedor recebe 200 por semana mais 9% de suas vendas brutas aquela semana
# ex: 3000, recebe 200+ 9% de 3000 =470
# array de contadores, determine quantos vendedores receberam salários nos seguintes intervalos:
# 200-299; 300-399; 400-499; 500-599; 600-699; 700-799; 800-899; 900-999; 1000...
# Crie uma formula para chegar na posição da lista a partir do salário, sem usar vários if aninhados

import random

salarios = []
margens = ["200-299", "300-399", "400-499", "500-599", "600-699", "700-799", "800-899", "900-999", "1000 ou mais"]
contador = [0] * 9

for i in range (15):
    salarios.append(random.uniform(200, 2000))

for salario in salarios:
    indice = int((salario-200)/ 100)
    indice = min(indice, 8)
    contador [indice] += 1

for i in range (len(contador)):
    print(str(contador[i])+" vendedores receberam salários na margem "+margens[i])
