n = int(input('Enter of a decimal no: '))
bin = 0
s = ""
while (n>0):
    r = n%2
    s = str(r) + s
    n = n//2
print(s)