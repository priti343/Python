list1= [2,3,4]
list2= [5,6,7]
list = list1+list2
print(list)
list = list+[11]
list1.extend([8,9,10])#exrend  method is a function that add the some number in ist
print(list1)
print(list)
list = list2+[44,55,66,77,88]#concatenation method
print(list)



#repetation method
rep = [1,2,4,5,5]
print(rep*5)
## in operator
list5 = [2,3,5,67,8]
print(4 in list5)
if 3 in list5:
    print('found')
else:
    print('not found')


    ## not in operator
if 4 not in list5:
    print('True')
else:
    print('False')
