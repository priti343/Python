from fractions import Fraction

print(Fraction(11,35))
f1 =Fraction(1,2)
print(f1)

f1=Fraction(23,42)
print(f1)

f2 = Fraction(23,33)
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)

L1=[(1,2),(4,9),(6,8)]
for n,d in L1:
    print('{}'.format(Fraction(n,d)))
