resto = float(input())
print('NOTAS:')

notas = resto/100
resto = resto%100
print(str(int(notas)) + ' nota(s) de R$ 100.00')

notas = resto/50
resto = resto%50
print(str(int(notas)) + ' nota(s) de R$ 50.00')

notas = resto/20
resto = resto%20
print(str(int(notas)) + ' nota(s) de R$ 20.00')

notas = resto/10
resto = resto%10
print(str(int(notas)) + ' nota(s) de R$ 10.00')

notas = resto/5
resto = resto%5
print(str(int(notas)) + ' nota(s) de R$ 5.00')

notas = resto/2
resto = resto%2
print(str(int(notas)) + ' nota(s) de R$ 2.00')

print('MOEDAS:')

notas = resto/1
resto = resto%1
print(str(int(notas)) + ' moeda(s) de R$ 1.00') 

notas = resto/0.50
resto = resto%0.50
print(str(int(notas)) + ' moeda(s) de R$ 0.50') 

notas = resto/0.25
resto = resto%0.25
print(str(int(notas)) + ' moeda(s) de R$ 0.25')

notas = resto/0.10
resto = resto%0.10
print(str(int(notas)) + ' moeda(s) de R$ 0.10')

notas = resto/0.05
resto = resto%0.05
print(str(int(notas)) + ' moeda(s) de R$ 0.05')

notas = round(resto*100)
print(str(int(notas)) + ' moeda(s) de R$ 0.01')    