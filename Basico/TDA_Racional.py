import fractions

qt = int(input())

for i in range(qt):
    entrada = input()
    n1, op1, d1, op, n2, op2, d2  = entrada.split(" ")
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    
    if op == "+":
        total = fractions.Fraction(n1*d2 + n2*d1) / (d1*d2)
        n1 = (n1*d2 + n2*d1)
        d1 = (d1*d2)
        
        if total.denominator == 1:
            print (str(n1)+"/"+str(d1)+" = "+ str(total)+"/1")
        else:
            print( str(n1)+"/"+str(d1)+" = "+ str(total))    
    elif op == "-":
        total = fractions.Fraction(n1*d2 - n2*d1) / (d1*d2)
        op1 = (n1*d2 - n2*d1)
        op2 = (d1*d2)
        
        if total.numerator == 0 and d1 == d2:
            print( str(op1)+"/"+str(op2)+" = "+ str(op1)+"/"+str(op2))
        elif total.denominator == 1:
            print (str(n1)+"/"+str(d1)+" = "+ str(total)+"/1")
        else:
            print( str(n1)+"/"+str(d1)+" = "+ str(total))
    elif op == "*":
        total = fractions.Fraction(fractions.Fraction(n1*d2) / fractions.Fraction(d1*d2))
        n1 = (n1*d2)
        d1 = (d1*d2)
        if total.denominator == 1:
            print (str(n1)+"/"+str(d1)+" = "+ str(total)+"/1")
        else:
            print( str(n1)+"/"+str(d1)+" = "+ str(total))
    else:
        total =  fractions.Fraction(fractions.Fraction(n1*d2) / fractions.Fraction(n2*d1))
        n1 = (n1*d2)
        d1 = (n2*d1)
        if total.denominator == 1:
            print (str(n1)+"/"+str(d1)+" = "+ str(total)+"/1")
        else:
            print( str(n1)+"/"+str(d1)+" = "+ str(total))
        