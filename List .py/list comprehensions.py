l1=[]
for x in range(10):
    l1.append(x)
print(l1)
l1 = [x for x in range(10)]
print(l1)
l2 = [x**2 for x in range(1,8)]
print(l2)
l3 = [x for x in (10,5,7,8,12,3) if x%2==0]
print(l3)
l4=[x.lower()for x in'Python']
print(l4)
l5 =[x for x in 'abc$&12@fgh12i'if x.isalpha()]
print(l5)