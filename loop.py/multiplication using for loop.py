n = int(input("Enter the value: "))
for count in range(1,11):
    print(n,'X',count,'=',count*n)
# factorial number
n = int(input("Enter the value: "))
fact = 1
for count in range(1,n+1):
    fact = fact * count
print('Factorial',n,'is',fact)