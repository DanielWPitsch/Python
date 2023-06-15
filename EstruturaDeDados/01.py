'''
 Função : Base de dados com lista encadeada
 Autor : Daniel Warella Pitsch
 Data : 14/06/23
 Observações: 
'''


#from noh import Noh

class Noh:
    def __init__(self, livro):
        self.livro = livro
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeça = None

    def estahVazia(self):
        return self.cabeça == None
        
    def insere(self, livro):
        novo_noh = Noh(livro) 
        if(self.estahVazia()):
            self.cabeça = novo_noh
        else:
            noh_atual = self.cabeça
            while (noh_atual.proximo):
                noh_atual = noh_atual.proximo
            noh_atual.proximo = novo_noh

    def remove(self, livro):
        if self.estahVazia():
            return
        if(self.cabeça.livro == livro):
            self.cabeça = self.cabeça.proximo
            return
        noh_atual = self.cabeça
        while(noh_atual.proximo):
            if(noh_atual.proximo.livro == livro):
                noh_atual.proximo = noh_atual.proximo.proximo
                return
            noh_atual = noh_atual.proximo

    def edita(self, Noh):
        escolha = input("Informe o atributo que deseja alterar?"+
                        "\n-autor"+
                        "\n-titulo"+
                        "\n-editora"+
                        "\n-ano"+
                        "\n-nenhum\n")
        if(escolha == "nenhum"):
            return  
        Noh.livro[escolha] = input("Informe a alteração em "+escolha+": ")

    #busca por titulo ou autor dado pela chave no parametro da função
    def buscaNoh(self, entrada, chave):
        if self.estahVazia():
            return
        if(self.cabeça.livro[chave] == entrada):
            return self.cabeça
        noh_atual = self.cabeça
        while(noh_atual.proximo):
            if(noh_atual.proximo.livro[chave] == entrada):
                return noh_atual.proximo
        print("livro não encontrado")
        return 
    
    def mostrarLista(self):
        print("-Lista-")
        noh_atual = self.cabeça
        while noh_atual:
            print(noh_atual.livro)
            noh_atual = noh_atual.proximo

if __name__ == '__main__':
    
    livro1 = {"autor":"eu", "titulo":"math", "editora":"gg", "ano":87}
    livro2 = {"autor":"tu", "titulo":"geo", "editora":"gh", "ano":89}
    livro3 = {"autor":"ele", "titulo":"port", "editora":"ig", "ano":97}

    #inserindo e mostrando
    lista = ListaEncadeada()
    lista.insere(livro1)
    lista.insere(livro2)
    lista.insere(livro3)
    lista.mostrarLista()

    #removendo e mostrando
    lista.remove(livro2)
    lista.mostrarLista()

    #buscando por nome e printando
    noh = lista.buscaNoh("math", 'titulo')
    print("livro buscado por titulo:\n", noh.livro)
    
    #buscando por autor e printando
    noh2 = lista.buscaNoh("ele", 'autor')
    print("livro buscado por autor:\n", noh.livro)

    #editando
    lista.edita(noh)
    lista.mostrarLista()
    
