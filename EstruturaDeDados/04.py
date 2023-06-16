'''
 Função : Selection Sort
 Autor : Daniel Warella Pitsch
 Data : 16/06/23
 Observações: 
'''

def selectionSort(array):
    
    for indice in range(len(array)):
        min_index = indice
 
        for j in range(indice + 1, len(array)):
            # encontra o indice do menor valor 
            if array[j] < array[min_index]:
                min_index = j
         # trocando os elementos para ordenar o array
        (array[indice], array[min_index]) = (array[min_index], array[indice])
 
array1 = [-2, 45, 0, 11, -9,88,-97,-202,747]
selectionSort(array1)
print('Array ordenado:\n', array1)
