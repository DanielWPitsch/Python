
pi = 3.14159

entrada = input().split()
a,b,c = float(entrada[0]), float(entrada[1]), float(entrada[2])

        
a, b, c = (entrada.split(" "))
a, b, c= float(a), float(b), float(c)

print('TRIANGULO: {:.3f}'.format((a*c)/2))
print('CIRCULO: {:.3f}'.format(pi*(c*c)))
print('TRAPEZIO: {:.3f}'.format(((a+b)*c)/2))
print('QUADRADO: {:.3f}'.format(b*b))
print('RETANGULO: {:.3f}'.format(a*b))