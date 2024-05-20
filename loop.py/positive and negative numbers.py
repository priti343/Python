Num_of_no = int(input('Enter a number of number: '))
Psum = 0
Nsum = 0
count = 0
while count<Num_of_no:
    n = int(input('Enter number '))
    if n>0:
     Psum = Psum+n
    else:
     Nsum = Nsum+n
    count = count+1
print("Sum is positive : ",Psum)
print("Sum is Negative : ",Nsum)
