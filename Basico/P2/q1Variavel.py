#media de salario
#media de numero de filhos
#nome da pessoa que possui o maior e o menor salário
#percentual de pessoas com salário até 1500,00

somaFilhos=somaSalarios=salarioBaixo=qtdPessoas=maiorSalario=menorSalario=0
salario=1.0

while(True):
    salario=float(input("Qual o seu salário?"))
    if(salario<0):
        break
    nome=input("Qual o seu nome?")
    filhos=int(input("Quantos filhos tem?"))

    if(qtdPessoas==0):
        menorNome=nome
        maiorNome=nome
        maiorSalario=salario
        menorSalario=salario
    if(salario<=1500):
        salarioBaixo+=1
    if(salario>maiorSalario):
        maiorSalario=salario
        maiorNome=nome
    if(salario<menorSalario):
        menorSalario=salario
        menorNome=nome

    somaFilhos+=filhos
    somaSalarios+=salario
    qtdPessoas+=1

print(f'\n\nA média de filhos é: {"%.2f" %(somaFilhos/qtdPessoas)}')
print(f'A média dos salários é: {"%.2f" %(somaSalarios/qtdPessoas)}')
print("A pessoa com maior salário é:", maiorNome)
print("A pessoa com menor salário é:", menorNome)
print("O percentual de pessoas com salário menor que 1500 é:", (100/qtdPessoas)*salarioBaixo)