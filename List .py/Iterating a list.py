# using for loop acess all element
list1= [5,6,7,8,9]
for x in list1:
    print(x)
    # using range of for loop
for i in range(len(list1)):
    print(list1[i])
for i in range(2,len(list1)):#print index 2 se
    print(list1[i])


for i in range(len(list1)-1,-1,-1):
    print(list1[i])#reverse printing

# print negative indexes reverse index
list = [90,22,33,44,88]
for i in range(-1,-(len(list)+1),-1):
    print(list[i])


###while loop 
list5 = [5,6,7,8,9]
i =0
while i<len(list5):
    print(list5[i])
    i=i+1