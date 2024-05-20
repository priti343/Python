s = {1,2,3,4,5,6,7,8,9,10}
a = {1,2,3,5,7}
b = {5,7,9,10,11}
c = a|b#union
c1 = a&b#intersection
c2= a-b#difference
c3 = a^b#symetric
print(c,c1,c2,c3)
    
x = a<s #subset
x1 = a<=s#superset
x2 = b<s
x3 = a>s
x4= a == b

print(x,x1,x2,x3,x4)
print(10 in s)
print(19 not in s)
print(33 in s)
