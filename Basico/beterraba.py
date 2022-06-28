um=dois=0

for i in range (5):
    entrada = int(input("Você gosta de beterraba? Digite: \n1-Sim \n2-Não\n"))
    if entrada ==1:
        um +=1
    else:
        dois +=1

print(f"A quantidade de pessoas que gostam de betrraba são {um} e as que não gostam são {dois}")