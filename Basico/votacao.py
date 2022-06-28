# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
# Os códigos utilizados são: 1, 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex:
# 1-Jose/ 2- João/etc) 5-voto nulo, 6 - voto em branco.
# Faça um programa que calcule e mostre: 
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos;
# para finalizar o conjunto tem-se o valor zero... */) 

jose =0; joao=0; pedro=0; maria=0; nulo=0; branco=0; candidato=9


while candidato != 0:
    candidato = int(input("Qual candidato você deseja votar?\n 0-Encerrar votação\n 1-José\n 2-João\n 3-Maria\n 4-Pedro\n 5-Nulo\n 6-Branco\n"))
    
    if(candidato == 1):
        jose += 1
    elif(candidato ==2):
        joao += 1
    elif(candidato ==3):
        maria += 1
    elif(candidato ==4):
        pedro += 1
    elif(candidato ==5):
        nulo += 1
    elif(candidato ==6):
        branco += 1
    elif(candidato ==0):
        print("Fim da votação!")
    else:
        print("opcão inválida! (voto não computado)\nPor favor escolha uma das opções a seguir:")

total = jose+joao+maria+pedro+nulo+branco

print("O total de votos em José foi: ", jose)
print("O total de votos em João foi: ", joao)
print("O total de votos em Maria foi: ", maria)
print("O total de votos em Pedro foi: ", pedro)
print("O total de votos nulos foi: ", nulo)
print("O total de votos em Branco foi: ", branco)

print("A percentagem de votos nulos foi: {:.2f}".format(nulo/total))
print("A percentagem de votos em branco foi: {:.2f}".format(branco/total))
