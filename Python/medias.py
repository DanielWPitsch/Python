#while != 1
# Mostre a quantidade de valores que foram lidos;
# Exiba os valores na orderm em que foram informados, uma ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem.

somaValores=0; abaixoMedia=0; acimaMedia=0; nota=2
notas =[]

while(nota !=1):
    nota = float(input("Informe as notas(Ao concluir, digite 1): "))
    notas.append(nota)
    somaValores= somaValores +nota
    if(nota > 7):
        acimaMedia +=1
    elif(nota ==7):
        print("", end="")
    else:
        abaixoMedia
    
print("A média das notas é: {:.2f}".format(somaValores/len(notas)))
print("A quantidade de notas acima da média é:", acimaMedia)
for i in notas:
      print(i, end=" ")
reversa = reversed(notas)
for i in reversa:
    print(i)

print("\n-Fim!-")
