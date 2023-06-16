'''
 Função : Gerenciador de atendimento com fila
 Autor : Daniel Warella Pitsch
 Data : 16/06/23
 Observações: 
'''

class Atendimento:
    def __init__(self, max):
        self.paciente = [None] * max
        self.ordem = 0
        self.quantidade = 0
        
    def adicionar_paciente(self, paciente):
        if(self.quantidade < len(self.paciente)):
            self.paciente[self.quantidade] = paciente
            self.quantidade += 1
            
    def proximo_paciente(self):
        if(self.ordem >= 0):
            elemento = self.paciente[self.ordem]
            self.paciente[self.ordem] = None
            self.quantidade -= 1
            return elemento

    def vazia(self):
        return self.ordem == 0

    def exibe_fila(self):
        contador=0
        print("\n -Fila de pacientes- \n")
        while(contador < len(self.paciente)):
            print(self.paciente[contador], end="\n\n")
            contador += 1

    def quantidade_pacientes(self):
        return self.quantidade

if __name__ == '__main__':
    escolha =1
    
    tamanho = int(input("Qual o tamanho da fila de atendimento? "))
    fila = Atendimento(tamanho)
    
    while(escolha != 0):
        escolha = int(input("    -Menu-"+ 
                           "\nQual operação deseja fazer?"+
                           "\n1-Adicionar Paciente"+
                           "\n2-Proximo Paciente"+
                           "\n3-Quantidade de Pacientes a serem atendidos"+
                           "\n4-Sair\n"))
        if(escolha == 1):
            
            nome = input("Informe o nome do paciente a ser adicionado: ")
            fila.adicionar_paciente(nome)
            fila.exibe_fila()
            
        elif(escolha == 2):
            if(fila.vazia()):
               print("A pilha está vazia!")
            else:
                print("O cliente a ser atendido agora é:"+fila.proximo_cliente())
                fila.exibe_fila()
        elif(escolha == 3):
            print("A quantidade de pacientes a serem atendidos é:", fila.quantidade_pacientes())
        elif(escolha == 4):
            break
        else:
            print("Opção inválida!")
            
    print("-Fim-")
