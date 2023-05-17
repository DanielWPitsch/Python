dependencias = ['A', 'B', 'C', 'D', 'E']
exemplo = [[], [], [], [], []]
instalados = []

continuar =1
while(continuar != 0):
    letra= int(input("Informe em qual tem dependencia: \n1-A\n2-B\n3-C\n4-D\n5-E\n"))

    if(letra ==1):
        dep = input("A depende de qual dependencia? ")
        exemplo[0].append(dep)
    if(letra ==2):
        dep = input("B depende de qual dependencia? ")
        exemplo[1].append(dep)
    if(letra ==3):
        dep = input("C depende de qual dependencia? ")
        exemplo[2].append(dep)
    if(letra ==4):
        dep = input("D depende de qual dependencia? ")
        exemplo[3].append(dep)
    if(letra ==5):
        dep = input("E depende de qual dependencia? ")
        exemplo[4].append(dep)

    print("Deseja informar mais dependencias?")
    continuar = int(input("Digite 1 para continuar e 0 para sair: "))

contador = 0

while(contador < 4):
    for i in range(5):
        if(len(exemplo[i]) == 0 ):
            print(dependencias[i])
            if (not(dependencias[i] in instalados)):
                instalados.append(dependencias[i])
            for linha in range(5):
                for coluna in range(len(exemplo[linha])):
                    if(exemplo[linha][coluna] == dependencias[i]):
                        exemplo[linha].remove(dependencias[i])
                        break;
    contador += 1
        
print(instalados)
print(exemplo)
