pesos = []; alturas = []; codigos = []
entrada=1; contador=0
baixo = 1.99; alto=0
gordo=0; magro=999.99
mediaPesos=0; mediaAlturas=0

print("Cadastro de clientes")
while entrada !=0:
    codigos.append(int(input("Digite o codigo do cliente: ")))
    pesos.append(float(input("Digite o peso do cliente: ")))
    alturas.append(float(input("Digite a altura do cliente: ")))
    
    if alto<alturas[contador]:
        alto=alturas[contador]
    if baixo>alturas[contador]:
        baixo = alturas[contador]
    if gordo<pesos[contador]:
        gordo=pesos[contador]
    if magro>pesos[contador]:
        magro = pesos[contador]

    mediaPesos= mediaPesos + pesos[contador]
    mediaAlturas= mediaAlturas + alturas[contador]
    
    entrada = int(input("Para parar, digite 0: "))
    contador+=1

mediaPesos = mediaPesos/contador
print(f'A média dos pesos é: {"%.2f" %mediaPesos}')
mediaAlturas = mediaAlturas/contador
print(f'A média das alturas é: {"%.2f" %mediaAlturas}')

indice = alturas.index(alto)
print(f'O código do cliente mais alto é: {codigos[indice]}, sua altura é: {"%.2f" %alto} e seu peso é: {"%.2f" %pesos[indice]}.') 
indice = alturas.index(baixo)
print(f'O código do cliente mais baixo é: {codigos[indice]}, sua altura é: {"%.2f" %baixo} e seu peso é: {"%.2f" %pesos[indice]}.')
indice = pesos.index(gordo)
print(f'O código do cliente mais gordo é: {codigos[indice]}, sua altura é: {"%.2f" %alturas[indice]} e seu peso é: {"%.2f" %gordo}.')
indice = pesos.index(magro)
print(f'O código do cliente mais magro é: {codigos[indice]}, sua altura é: {"%.2f" %alturas[indice]} e seu peso é: {"%.2f" %magro}.')