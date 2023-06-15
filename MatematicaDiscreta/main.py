from math import factorial
from itertools import combinations
from itertools import permutations
from itertools import product
from collections import Counter

lista1 = ['A', 'B', 'C', 'D',]
lista2 = ['G', 'H', 'I']
lista3 = ['J', 'K', 'L', 'M', 'N']
lista4 = ['O', 'P']

n = len(lista1)
nova_lista = []
t = 0
opcao = 0

while opcao < 1 or opcao > 7:
    print("Opção Invalida! Escolha uma opção entre 1 e 7.")
    
    opcao = int(input("\n Escolha a opção desejada:"+
                  "\n 1 - Principio da Regra da Soma;"+
                  "\n 2 - Principio da Regra do Produto;"+
                  "\n 3 - Permutações: Quando r = n;"+
                  "\n 4 - Permutações: Amostras Ordenadas Com Repetições; "+
                  "\n 5 - Permutações: Amostras Ordenadas Com Reposição;"+
                  "\n 6 - Permutações: Amostras Ordenadas Sem Reposição;"+
                  "\n 7 - Combinações.\n "))

if opcao == 1:
    qtd_possibilidades = len(lista1) + len(lista2) + len(lista3) + len(lista4)
    nova_lista = lista1 + lista2 + lista3 + lista4


    print(f'\nA quantidade de possibilidades são {qtd_possibilidades}.')
    print(f"As {qtd_possibilidades} amostras possiveis são: ")
    for n in nova_lista:
        print(' '.join(n), end=" ")

elif opcao == 2:
    possibilidades = list(product(lista1, lista2, lista3, lista4))
    print(possibilidades)
    #t = len(possibilidades)
    qtd_possibilidades = len(lista1) * len(lista2) * len(lista3) * len(lista4)
    print(f'\nA quantidade de possibilidades são {qtd_possibilidades}.')
    print(f"As {qtd_possibilidades} amostras possiveis são:")
    for p in possibilidades:
        print(''.join(p), end=" ")
        
#permutações = fatorial; e r=n; 
elif opcao == 3:
    r = n
    possibilidades = factorial(n)

    permutações = list(permutations(lista1, r))

    print(f'\nA quantidade de permutações possíveis são {possibilidades}.')

    print(f"As {possibilidades} amostras possiveis são: ")

    for p in permutações:
        print(''.join(p), end=" ")

#permutações com repetições
elif opcao == 4:
    palavra = input('Digite uma palavra: ')
    n = len(palavra)
    contador = Counter(palavra)
    #usa função Counter de Colections para contar qauntas vezes cada letra ocorre na palavra
    print(f'\nA quantidade de letras encontradas na palavra: {palavra}, são: {contador}:')

    contador = list(contador.values())
    #contador recebe uma lista dos valores do dicionario criado pela função Counter
    m = factorial(n)

    for c in contador:
        m //= factorial(c)
        #dividindo pela ocorrencia de cada letra

    print(f'\nA quantidade de permutações possíveis são {m}.')

    print(f"As {m} amostras possiveis são: ")

    permutações = set(permutations(palavra, n))
    #set aqui é usado pois ele não aceita elementos duplicados

    for p in permutações:
        print(''.join(p), end=" ")

#Permutações: Amostras Ordenadas Com Reposição
elif opcao == 5:
    r = int(input("\nDigite o tamanho das amostras desejado: "))
    while r < 1 or r > n:
        print(f'\nOpção Inválida!! Digite uma opção entre 1 e {n - 1}.')
        r = int(input("\nDigite o tamanho das amostras desejado: "))

    combinações = pow(n, r)

    combinations = list(product(lista1, repeat=r))
    # a lista de amostra será multiplicada pelo tamanho desejado
    t = len(combinations)
    print(f'\nA quantidade de permutações possíveis são {t}.')
    print(f"As {t} amostras possíveis são: ")
    for c in combinations:
        print(''.join(c), end=" ")

#Permutações: Amostras Ordenadas sem Reposição
elif opcao == 6:
    r = int(input("\nDigite o tamanho das amostras desejado: "))
    while r < 1 or r >= n:
        print(f'\nOpção Inválida!! Digite uma opção entre 1 e {n - 1}.')
        r = int(input("\nDigite o tamanho das amostras desejado: "))
    possibilidades = factorial(n) // factorial(n - r)

    permutações = list(permutations(lista1, r))

    print(f'\nA quantidade de amostras ordenadas sem reposição são {possibilidades}.')
    print(f"As {possibilidades} amostras possiveis são: ")

    for p in permutações:
        print(''.join(p), end=" ")


elif opcao == 7:
    r = int(input("\nDigite o tamanho das amostras desejado: "))
    while r < 1 or r > n:
        print(f'\nOpção Inválida!! Digite uma opção entre 1 e {n}.')
        r = int(input("\nDigite o tamanho das amostras desejado: "))
    combinação = factorial(n) // (factorial(r) * factorial(n - r))

    print(f'\nO número de amostras possíveis são {combinação}.')

    combinações = list(combinations(lista1, r))

    print(f"As {combinação} amostras possiveis são: ")

    for c in combinações:
        print(''.join(c), end=" ")
