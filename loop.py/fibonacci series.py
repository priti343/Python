n = int(input('Enter the no. of terms: '))
a = 0
b = 1
# a , b ,(c = a+b)
# 0  1  ;0+1=1
# 1  1  ;1+1=2
#1   2  ;1+2=3
#2   3  ;2+3=5
#3   5  ;3+5=8
for i in range(n):
    print(a)
    a = b
    c = a+b
    b = c