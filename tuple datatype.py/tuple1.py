tuple = (10)
print(tuple)
print(type(tuple))# its give the int type because this is not take as a tuple
t1 = (10,)
print(type(t1))# it s print tuple type of data because in there seperate the (,).
t2 = (4,3,5,6,7,8,9,24)
a,b,c,d,e,f,g,h=t2
print(t2)
t3=[x for x in range(10)]
print(t3)
print(type(t3))
'''tuple= tuple(x for x in range(10)) 
print(tuple)
print(type(tuple))'''
t4 = (*(x for x in 'Python'),)
print(t4)
print(type(t4))
