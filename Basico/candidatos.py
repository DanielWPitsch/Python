lula=0; bolsonaro=0; ciro=0; nulo=0; voto=0

quantidadeEleitores = int(input("Digite a quantidade de eleitores: "))

for i in range(quantidadeEleitores):
    voto = int(input("Escolha o numero do respectivo candidato: \n13-Lula \n17-Bolsonaro \n12-Ciro \n"))
    if voto == 13:
        lula+=1
    elif voto ==17:
        bolsonaro+=1
    elif voto ==12:
        ciro+=1
    else:
        nulo+=1

print(f'Resultado: \nLula: {lula} \nBolsonaro: {bolsonaro} \nCiro: {ciro}')
