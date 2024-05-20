#pop() or del method
l1= [5,6,7,8,9]
l1.pop()
print(l1)
l1.pop(3)
print(l1)
del l1[2]
print(l1)
# there are use slicing
l2 = [8,9,6,4,5,3]
del l2[0:4]
print(l2)
### remove()method
list = [1,2,3,4,2,3,4]
list.remove(2)# 2 is two times but there are remove only one(2)
#and duplicate value of 2 in there
print(list)


## clear()method
list3=[8,8,5,4,5,3,2]
list3.clear()
print(list3)
del list3[:]
print(list3)