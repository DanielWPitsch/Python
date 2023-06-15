'''
Função : Pilha de numeros reais
Autor : Daniel Warella Pistch
Data : 15/06/23
Observações: menu com push, pop, exibir a pilha a cada operação,
verificar se a pilha está vazia
'''


class Pilha:
    def __init__(self, max):
        self.dados = [None] * max
        self.topo = -1

    def empilha(self, elemento):
        #se topo for menor que o tamanho-1, quer dizer que tem espaço
        if(self.topo < len(self.dados)-1):
            self.topo += 1
            self.dados[self.topo] = elemento
            
    def desempilha(self):
        if(self.topo >= 0):
            elemento = self.dados[self.topo]
            self.topo -= 1
            return elemento

    def vazia(self):
        return self.topo == -1

    def exibe_pilha(self):
        print("Pilha completa", self.dados)

if __name__ == '__main__':
    esolha =1
    
    tamanho = input(int("Qual o tamanho da pilha? "))
    pilha = Pilha(tamanho)
    
    while(escolha != 0):
        esolha = input(int("    -Menu-"+ 
                           "\nQual operação deseja fazer na pilha"+
                           "\n1-Empilha"+
                           "\n2-Desempilha"+
                           "\n3-Sair"))
        if(escolha == 1):
            entrada = (input("Informe o elemento a ser empilhado: ")
            pilha.empilha(entrada)
        elif(escolha == 2):
            print("O elemento "+desempilha+" foi desempilhado")
            exibe_pilha()
        elif(escolha == 0):
            break
        else:
            print("Opção inválida!")
