import math
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
root1 = (- b + math.sqrt(b**2 - 4 * a * c))/(2*a)
root2 = (- b - math.sqrt(b**2 - 4 * a * c))/(2*a)
print(root1)
print(root2)