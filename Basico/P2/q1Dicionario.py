#media de salario
#media de numero de filhos
#nome da pessoa que possui o maior e o menor salário
#percentual de pessoas com salário até 1500,00

dicionario={}; maiorSalarioDic={}; menorSalarioDic={}
qtdPessoas=maiorSalario=menorSalario=somaFilhos=somaSalarios=salarioBaixo=0

while(True):
    lista=[]
    salario=float(input("Digite seu salário: "))
    if(salario<0):
        break
    lista.append(salario)
    lista.append(input("Digite seu nome: "))
    filhos=(int(input("Digite a quantidade de filhos que tem: ")))
    lista.append(filhos)
    dicionario[qtdPessoas]=lista

    if(qtdPessoas==0):
        maiorSalarioDic[0]=lista
        menorSalarioDic[0]=lista
    if(salario>maiorSalario):
        maiorSalario =salario
        maiorSalarioDic[0]=lista
    if(salario<menorSalario):
        menorSalario =salario
        menorSalarioDic[0]=lista
    if(salario<1500):
        salarioBaixo+=1

    qtdPessoas+=1
    somaFilhos+=filhos
    somaSalarios+=salario

print("Nome da pessoa com maior salario:", maiorSalarioDic[0][1])
print("Nome da pessoa com menor salario:", menorSalarioDic[0][1])
print(f'A média de filhos é: {"%.2f" %(somaFilhos/qtdPessoas)}')
print(f'A média de salários é: {"%.2f" %(somaSalarios/qtdPessoas)}')
print(f'{"%.2f" %(salarioBaixo*100/qtdPessoas)}% de pessoas tem salário abaixo de 1500 reais')