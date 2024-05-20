L1 = [2,3,5,6,9,8,6,5,5,3,3]
L2 =[]
for x in L1:
    if x not in L2:
        L2.append(x)
print(L2)

## concatenate all integer from a list to a single number
l1=[3,4,5,6,7]
s1 = ''
for x in l1:
    s1 += str(x)
print(int(s1))


### OVERLAPPING list
l1 = [10,15,6,9,12,8,4]
l2 =[14,6,19,4,7,10,11]
l3 =[]
for x in l1:
    if x in l2:
        l3.append(x)
print(l3)


## find the number of occurrences of each item
l1 = ['A','B','C','D','E','A','B','C','D','E']
result = []
for item in l1:
    if item not in result:
        result.append(item)
        count=l1.count(item) 
        
        result.append(count)
print(result)



## Telegram: string to morse code



####adding two matrix
l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
l3 = []
for i in range(3):
    s = []
    for j in range(4):  
     r = l1[i][j]+l2[i][j]
     s.append(r)     
    l3.append(s)
print(l3)




##### transpose of a matrix
l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(4):
    s = []
    for j in range(3):
        s.append(l1[j][i])
    l2.append(s)
    print(l2)
l1= [1 , [2,3,] ,4  , 5 , [6,7] ,[ 8 ,9] ,10 ]
print(l1)
list[5]