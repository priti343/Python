list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[4])#index method
print(list[-4])
x=list[3]=90
print(x)
print(list)
print(list[:])#slice method start
print(list[3:])#starting point
print(list[3:5])#ending point
print(list[0:10:8])
print(list[0:10:2]) 
print(list[0:10])
print(list[0:9])
print(list[::-1])#reverse list
print(list[-1:-11:-1])#reverse list
print(list[-1:-11:-2])#print 2nd number
print(list[-1:-11:-3])#print 3rd number

### replace  the number in list
list2 = [1,2,3,4,5,6,7,8,9,10]
print(list2)
list2[0:3]=[10,20]
print(list2)
list2[0:2]=[10,20,30,40,50]
print(list2)
list2[::2]=[11,22,33,44,55,66]#alternate elements are change
print(list2)