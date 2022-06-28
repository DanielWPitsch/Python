import fractions

f1 = fractions.Fraction(input())
f2 = fractions.Fraction(input())

n1 = f1.numerator
n2 = f2.numerator

d1 = f1.denominator
d2 = f2.denominator

total = (n1*d2 + n2*d1) / (d1*d2)
ntemp = (n1*d2 + n2*d1)
dtemp =  (d1*d2)
print( str(ntemp)+"/"+str(dtemp)+" = "+ str(fractions.Fraction(total)))

total = (n1*d2 - n2*d1) / (d1*d2)
ntemp = (n1*d2 - n2*d1)
dtemp = (d1*d2)
print( str(ntemp)+"/"+str(dtemp)+" = "+ str(fractions.Fraction(total)))

total = (n1*d2) / (d1*d2)
ntemp = (n1*d2)
dtemp = (d1*d2)
print( str(ntemp)+"/"+str(dtemp)+" = "+ str(fractions.Fraction(total)))

total = (fractions.Fraction(n1/d1) / fractions.Fraction(n2/d2))
ntemp = (n1*d2)
dtemp =  (n2*d1)
print( str(ntemp)+"/"+str(dtemp)+" = "+ str(fractions.Fraction(total)))