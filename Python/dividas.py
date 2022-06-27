# Faça um programa que recebe o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da divida, valor do juros, quantidade de parcelas, valor da parcela
# Os juros e a quantidade de parcelas se guem a tabela abaixo:
# Quantidade de parcelas % de juros sobre o valor inicial da dívida:
# 1 parcela 0%; 3 parcelas; 10%; 6 parcelas 15%; 9 parcelas 20%; 12 parcelas, 25%
# Exemplo de saída do programa:
# Valor da Divida, Valor dos juros, Quantidade de parcelas, Valor da Parcela;
# R$ 1.000,00, 01 R$ 1.000,00; R$ 1.100,00 100 3 R$366,00; R$ 1.150,00; 150 6 R$191,67;

divida = float(input("Digite o valor da divida: "))

print("Divida de "+str(divida)+" para ser paga em 1 parcela sem juros, ou seja:", divida)
print("Divida de {:.2f}".format(divida+(divida*0.10))+" para ser paga em 3 parcelas com 10% de juros, saindo cada parcela a: {:.2f}".format((divida+(divida*0.10))/3))
print("Divida de {:.2f}".format(divida+(divida*0.15))+" para ser paga em 6 parcelas com 15% de juros, saindo cada parcela a: {:.2f}".format((divida+(divida*0.15))/6))
print("Divida de {:.2f}".format(divida+(divida*0.20))+" para ser paga em 9 parcelas com 20% de juros, saindo cada parcela a: {:.2f}".format((divida+(divida*0.20))/9))
print("Divida de {:.2f}".format(divida+(divida*0.25))+" para ser paga em 12 parcelas com 25% de juros, saindo cada parcela a: {:.2f}".format((divida+(divida*0.25))/12))
