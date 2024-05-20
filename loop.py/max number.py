num_of_no = int(input("enter max no: "))
count = 0
max = int(input('Enter the max number: '))

while count>num_of_no -1:
    n = int(input('Enter value:'))
    if n > max:
        max = n
    count = count + 1
print('Max number is',max)