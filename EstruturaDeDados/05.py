'''
 Função : Gerenciador de pilha de processos
 Autor : Daniel Warella Pitsch
 Data : 16/06/23
 Observações: 
'''

class Pilha:
    def __init__(self, maximo):
        self.identificador = maximo * [None]
        self.descrição = maximo * [None]
        self.topo = -1

    def empilha(self, identificador, descrição):
        if(self.topo < len(self.identificador)-1):
            self.topo += 1
            self.identificador[self.topo] = identificador
            self.descrição[self.topo] = descrição
            
    def desempilha(self):
        if(self.topo >= 0):
            removido = []
            removido.append(self.identificador[self.topo])
            removido.append(self.descrição[self.topo])
            self.identificador[self.topo] = None
            self.descrição[self.topo] = None
            self.topo -= 1
            return removido

    def vazia(self):
        return self.topo == -1

    def exibePilha(self):
        print("\n -Lista de processos- \n")
        for indice in range(len(self.descrição)):
            print("Id: "+str(self.identificador[indice]))
            print("Descrição: "+str(self.descrição[indice]))
            print()

    def encerrar(self):
        while(self.topo != -1):
            self.identificador[self.topo] = None
            self.descrição[self.topo] = None
            self.topo -= 1
        print("\nLimpando Pilha de processos...")

if __name__ == '__main__':
    escolha =1
    
    tamanho = int(input("Qual o tamanho da pilha de proceesos? "))
    pilha = Pilha(tamanho)
    
    while(escolha != 0):
        escolha = int(input("    -Menu-"+ 
                           "\nQual operação deseja fazer?"+
                           "\n1-Adicionar Processo"+
                           "\n2-Retirar Processo"+
                           "\n3-Encerrar\n"))
        if(escolha == 1):
            
            identificador = input("Informe o id do processo a ser adicionado: ")
            descrição = input("Informe a descrição do processo: ")
            pilha.empilha(identificador, descrição)
            pilha.exibePilha()
            
        elif(escolha == 2):
            if(pilha.vazia()):
               print("A pilha está vazia!")
            else:
                pop = str(pilha.desempilha())
                print("Removido o processo de"+
                      "Id: "+pop[0]+
                      "\nDescrição: "+pop[1]+
                      "\nfoi desempilhado com sucesso!\n")
                pilha.exibePilha()
            
        elif(escolha == 3):
            pilha.encerrar()
            pilha.exibePilha()
            break
        else:
            print("Opção inválida!")
            
    print("-Fim-")
