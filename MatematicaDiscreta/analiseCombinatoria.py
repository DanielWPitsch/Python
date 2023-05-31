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
    permutacaoR = fatorial(len(nome)) / (fatorial(len(nome)) - fatorial(r))
    print("permutação r < n: ", permutacaoR)

    #3.Quando os elementos podem se repetir
    # fatorial(elementos) / fatorial(repetido1) * fatorial(repetido2)...
    palavra="banana"
    contador = Counter(palavra)
    print(contador)
                   
    #4. Amostra com reposição = n^r
    reposicao = pow(2, 3) #pow(n, r)
    print("reposicao", reposicao)

    #6 Combinações
    combinacao = list(itertools.combinations(numeros, 2)) 
    print("combinações: \n", combinacao)
    print(len(combinacao), "combinações\n")

    
    

if __name__ == "__main__":
    sys.exit(main())
    
