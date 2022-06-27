
pi = 3.14159

entradas=input().split()
a,b,c = float(entradas[0]), float(entradas[1]), float(entradas[2])


print('TRIANGULO: {:.3f}'.format((a*c)/2))
print('CIRCULO: {:.3f}'.format(pi*(c**2)))
print('TRAPEZIO: {:.3f}'.format(((a+b)*c)/2))
print('QUADRADO: {:.3f}'.format(b**2))
print('RETANGULO: {:.3f}'.format(a*b))