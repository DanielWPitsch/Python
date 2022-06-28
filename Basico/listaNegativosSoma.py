lista = []
contador=soma=0

for i in range (4):
    lista.append(int(input("Digite o "+str(i+1)+"º número: ")))
    if lista[i] <0:
        contador+=1
    else:
        soma = soma + lista[i]
        
print("A soma dos numeros positivos é: ",soma)
print(f"A lista contém {contador} números negativos")