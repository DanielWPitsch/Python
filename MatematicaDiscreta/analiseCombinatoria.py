import sys
import itertools
import math
from collections import Counter

def fatorial(n):
    return 1 if (n==1 or n==0) else n * fatorial(n - 1);
        
def main():
    numeros = [1, 2, 3, 4]
    nome = ['b', 'a', 'n', 'a']

    #1. Permutação onde n = r
    permutacoes = list(itertools.permutations(nome, 3))
    print("permutações: \n",permutacoes)
    print(len(permutacoes), "permutações\n")
    

    #2 e 5.Permutação onde r < n, sem reposição 
    r= 2
    permutacaoR = fatorial(len(nome)) / fatorial(len(nome) - r)
    print("permutação r < n (sem reposição): \n", permutacaoR)
    #r determina loops do for interno
    #a variavel permutacaoR determina os loops do for externo
    #cada loop interno insere 1 elemento numa lista
    #cada loop externo insere uma lista na lista
    #condição de não por elementos iguais
    

    #3.Quando os elementos podem se repetir e r=n
    # fatorial(elementos) / fatorial(repetido1) * fatorial(repetido2)...
    palavra="banana"
    contador = Counter(palavra)
    #achando fatorial divisor
    divisor=1
    for each in contador:
        if(contador[each] > 1):
            divisor *= fatorial(contador[each])
    repetir= fatorial(len(palavra)) / divisor
    print("\npermutação quando os elementos podem se repetir: \n", repetir)

                   
    #4. Amostra com reposição = n^r
    reposicao = pow(12, 3) #pow(n, r)
    print("\nAmostra com reposicao: \n", reposicao)
    #smpre a mesma amostra repetindo r vezes
    #quantas maneiras possiveis de reorganizar?
    

    #6 Combinações
    combinacao = list(itertools.combinations(numeros, 2)) 
    print("\nCombinações: \n", combinacao)
    print(len(combinacao), "combinações\n")
    

if __name__ == "__main__":
    sys.exit(main())
    
