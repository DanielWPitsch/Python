'''
Função : Multiplicação de conjuntos
Autor : Daniel Warella Pitsch
Data : 17/05/2023
Observações: Dado n quantidade de listas, recebe a quantidade de possibilidades e as imprime
'''

from math import prod

#listas =[['aaaa','bbbb','cccc'], ['as', 'kl', 'op'], ['pp','ll', 'kk']]
listas = []
print("Cadastre duas ou mais listas de jogos de diferentes consoles")

qntListas = int(input("Quantas listas de jogos você deseja criar? "))

while(qntListas > 0):
    jogos = []
    qntJogos = int(input("Você deseja cadastrar 1, 2 ou 3 jogos? "))
    while(qntJogos > 0):
        nome = input("Informe o nome do jogo: ")
        jogos.append(nome)
        qntJogos -= 1
    listas.append(jogos)
    qntListas -= 1

tamanho = len(listas)
i=0
tamanhos = []
print("Jogos: ")
while(tamanho > 0):
    print(listas[i])
    tamanhos.append(len(listas[i]))
    i+=1
    tamanho-=1

if(len(listas) == 1):
    print(f'{sum(tamanhos)} possibilidades --> ', end="")
    for i in range(len(listas)):
        for k in range(len(listas[i])):
            print(f'{listas[i][k]}, ', end="")
else:
    print(f'{prod(tamanhos)} possibilidades --> \n', end="")

    while(len(listas) > 1):
        auxiliar = []
        aux=0;

        for i in range(len(listas[1])):
            for k in range(len(listas[0])):
                if(len(listas) == 2):
                    auxiliar.append(listas[0][k] +" e "+ listas[1][aux])
                else:
                    auxiliar.append(listas[0][k] +", "+ listas[1][aux])
            aux +=1
        listas[0] = auxiliar
        listas.pop(1)

print(listas[0])

