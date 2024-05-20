#append(x)
L1 = [5,6,7,8,9]
print(len(L1))
L1.append(10)
print(len(L1))
print(L1)
# list.append() takes exactly one argument(3 given) L1.append(11,33,44)print(L1)
l2=[9,8,7,6]#appending can be done using slicing also by using length of a list.
l2[6:6]=[12]
print(l2)



# extend() method(iterable)
list8 = [9,7,5,4,3,0]
print(list8)
list8.extend([98,56,445])
#second method
print(list8)
#third method
list8.extend('abc')
print(list8)
#extending use slicing method also
list8[len(list8):]=[12,33,44]
print(list8)



## insert(i,x)method
# i--index,x-- element
list0=[1,2,3,4,5]
print(id(list0))
print(list0)
list0.insert(0,10)
print(list0)
print(id(list0))
list0.insert(4,77)
print(list0)
list0[4:4]=[99]#so you can use slicing also for insertion
print(list0)




#### copy() method
l3= [6,7,8,9]
l2 = l3.copy()
print(l2)
print(l3)
print(id(l2))
print(id(l3))

