lista =[1,2,3,4,5]

for i in range(len(lista)):
    print(i)
print("\n")
for item in lista:
    print(item)

tabela = {
    'Maria' : {'Nota1':5, 'Nota2':6.5},
    'Pedro' : {'Nota1':8, 'Nota2':10},
    'Rafael' : {'Nota1':9, 'Nota2':7.5}
    }

print(tabela['Rafael']['Nota2'])
