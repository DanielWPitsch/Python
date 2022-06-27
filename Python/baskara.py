import math

def Raizes_Eq_2_Grau():
    A = int(input("Insira A: "))
    B = int(input("Insira B: "))
    C = int(input("Insira C: "))
    delta = math.pow(B,2)-(4*A*C)
    if(delta >= 0):
        x1 = (-B+math.sqrt(delta))/(2*A)
        x2 = (-B-math.sqrt(delta))/(2*A)
        print(f'x1 = {"%.2f" %x1} \nx2 = {"%.2f" %x2}')
    else:
        print("Não há raizes reais")

Raizes_Eq_2_Grau()
