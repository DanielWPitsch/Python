def fat(numero):
    
    if(numero == 1 or numero == 0):
        return 1
    else:
        return numero * fat(numero-1)
        
def main():
    n = int(input("informe o nomero: "))
    
    while(0 <= n):
        print(fat(n))
        n = n-1
main()
