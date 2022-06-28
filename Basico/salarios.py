import random

salarios = []
margens = ["200-299", "300-399", "400-499", "500-599", "600-699", "700-799", "800-899", "900-999", "1000 ou mais"]
contadores = [0]*9

for i in range (15):
    salarios.append(random.uniform(200, 1600))
    indice = int((salarios[i]-200)/100)
    if(indice>8):
        indice=8
    contadores[indice]+=1

for i in range(len(contadores)):
    print(f'{contadores[i]} vendedores receberam salários na margem: {margens[i]}')
