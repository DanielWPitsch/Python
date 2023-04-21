# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
transposta = []
for i in range (len(matrix[0])):
    linha=[]
    for k in range (len(matrix)):
        linha.append(matrix[k][i])
    transposta.append(linha)
print(transposta)

#Solução 2
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
