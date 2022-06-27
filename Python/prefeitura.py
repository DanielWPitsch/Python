import random

salarios =[]; nomes = []; filhos=[]
percentual=0

for i in range (5):
    salarios.append(random.uniform(800, 2500))
    filhos.append(random.randrange(0,8))
    nomes.append(input("Digite o nome do cidadao: "))
    if salarios[i]>1499:
        percentual+=1

print(f'A média salarial é R$ {"%.2f" %(sum(salarios)/len(nomes))} ')
print(f"A porcentagem de quem tem salario a partir de R$ 1500,00 é: {(percentual*100/len(nomes))}%" )
print("A media dos fihos da população é:", sum(filhos)/len(nomes))
mM = max(salarios)
indice = salarios.index(mM)
print("O nome da pessoa com maior salário é: "+nomes[indice])
mM = min(salarios)
indice = salarios.index(mM)
print("O nome da pessoa com menor salário é: "+nomes[indice])