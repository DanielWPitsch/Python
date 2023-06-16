'''
 Função : Gerenciador de pilha de processos
 Autor : Daniel Warella Pitsch
 Data : 16/06/23
 Observações: 
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
            self.dados[self.topo] = None
            self.topo -= 1
            return elemento

    def vazia(self):
        return self.topo == -1

    def exibe_pilha(self):
        print("Pilha completa", self.dados)

if __name__ == '__main__':
    escolha =1
    
    tamanho = int(input("Qual o tamanho da pilha? "))
    pilha = Pilha(tamanho)
    
    while(escolha != 0):
        escolha = int(input("    -Menu-"+ 
                           "\nQual operação deseja fazer na pilha"+
                           "\n1-Empilhar"+
                           "\n2-Desempilhar"+
                           "\n3-Sair\n"))
        if(escolha == 1):
            entrada = input("Informe o elemento a ser empilhado: ")
            pilha.empilha(entrada)
        elif(escolha == 2):
            print("O elemento "+str(pilha.desempilha())+" foi desempilhado!")
            pilha.exibe_pilha()
        elif(escolha == 3):
            break
        else:
            print("Opção inválida!")
