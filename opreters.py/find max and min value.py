numbers=[2,3,4,63,67,74]
max=numbers[0]
min=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i]<min:
        min=numbers[i]
print('Max:',max)
print('min:',min)




no1=[33,23,67,-24,-1,-87]
max=no1[0]
min=no1[0]
for i in range(len(no1)):
    if no1[i]>max:
        max=no1[i]
    elif no1[i]<min:
        min=no1[i]
print("Max:",max)
print('min:',min)

#mulltiply array with any number
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr*100)

#sort aray 
array1=[3,56,74,22,44]
n=len(array1)
for i in range(0,n):
    for j in range(i+1,n):
        if(array1[i]>array1[j]):
            temp=array1[i]
            array1[i]=array1[j]
            array1[j]=temp
print(array1)

