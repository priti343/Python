tuple = ('jps',54,34.53,5+5j,True,45)
for i in tuple:
    print(tuple)
for i in range(len(tuple)):
    print(tuple[i])
# index and slicing in tuple

print(tuple[-1])
print(tuple[-2])
print(tuple[:])
print(tuple[3:])
print(tuple[3:len(tuple):-1])
print(tuple[-3:-len(tuple):-1])
print(tuple[::-1])
print(tuple[::2])
# concenation and repetion 
t1 = (1,3,4,4)
t2 = (3,4,5,6)
print(t1+t2)
print(t1)
tuple = t1 + (9,8,7)
print(tuple)
print(t1*3)#repeation
temp = t2*4
print(temp)
#membership in or not in

print(3 in temp)
print(233 not in t1)
print(5 not in t1)
