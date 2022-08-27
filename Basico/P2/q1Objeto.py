#media de salario
#media de numero de filhos
#nome da pessoa que possui o maior e o menor salário
#percentual de pessoas com salário até 1500,00

class Pessoa:
    def __init__(self, salario, nome, filhos):
        self.salario = salario
        self.nome=nome
        self.filhos = filhos
    def getNome(self):
        return self.nome

def main():
    pessoas=[]
    somaFilhos=somaSalarios=salarioBaixo=qtdPessoas=maiorSalario=menorSalario=0
    salario=1.0
    pessoaPadrao=Pessoa(1.0,"",0)
    maiorSalarioPessoa=pessoaPadrao
    menorSalarioPessoa=pessoaPadrao
        
    while(True):
        salario=float(input("Qual o seu salário?"))
        if(salario<0):
            break
        
        nome=input("Qual o seu nome?")
        filhos=int(input("Quantos filhos tem?"))
        pessoa=Pessoa(salario,nome, filhos)
        pessoas.append(pessoa)

        if(qtdPessoas==0):
            maiorSalarioPessoa=pessoa
            menorSalarioPessoa=pessoa
            print("aqui")
        if(salario>maiorSalario):
            maiorSalario =salario
            maiorSalarioPessoa=pessoa
        if(salario<menorSalario):
            menorSalario =salario
            menorSalarioPessoa=pessoa
        if(salario<=1500):
            salarioBaixo+=1

        somaFilhos+=filhos
        somaSalarios+=salario
        qtdPessoas+=1

    print(f'\n\nA média de filhos é: {"%.2f" %(somaFilhos/qtdPessoas)}')
    print(f'A média dos salários é: {"%.2f" %(somaSalarios/qtdPessoas)}')
    print("A pessoa com maior salário é:", maiorSalarioPessoa.getNome())
    print("A pessoa com menor salário é:", menorSalarioPessoa.getNome())
    print("O percentual de pessoas com salário menor que 1500 é:", (100/qtdPessoas)*salarioBaixo)

# Executa o programa
if __name__ == "__main__":
    main()