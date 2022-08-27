#media de salario
#media de numero de filhos
#nome da pessoa que possui o maior e o menor salário
#percentual de pessoas com salário até 1500,00

salarios=[];nomes=[]
somaFilhos=somaSalarios=salarioBaixo=0
salario=1.0

while(True):
    salario=float(input("Qual o seu salário?"))
    if(salario<0):
        break
    salarios.append(salario)
    nomes.append(input("Qual o seu nome?"))
    filhos=int(input("Quantos filhos tem?"))
    somaFilhos+=filhos
    somaSalarios+=salario
    if(salario<=1500):
        salarioBaixo+=1

print(f'\n\nA média de filhos é: {"%.2f" %(somaFilhos/len(nomes))}')
print(f'A média dos salários é: {"%.2f" %(somaSalarios/len(nomes))}')
indiceMax=salarios.index(max(salarios))
indiceMin=salarios.index(min(salarios))
print("A pessoa com maior salário é:", nomes[indiceMax])
print("A pessoa com menor salário é:", nomes[indiceMin])
print("O percentual de pessoas com salário menor que 1500 é:", (100/len(nomes))*salarioBaixo)