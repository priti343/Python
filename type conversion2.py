# there are two type of conversion
#implicit
#explicit
i = 34
f = 34.4
b = True
c = 3+8j
s1 = 'johan'
s2 = '264'
x = int(f)
print(x)
y = float(i)
print(y)
b = int(True)
print(b)
#x = int(c)
#print(x) ganerete error because complex is not convert into int and float 
x = complex(i)
u = complex(f)
print(u)
print(x)
# string to float and complex or int
v = complex(s2)
print(v)
b = float(s2)
print(b)
n = int(s2)
print(n)
#float conversion
x = float(i)
#s = float(c)it is not cnverted
h = float(b)
#k = float(s1)  it is not converted
m = float(s2)
print(h)
#print(s)
print(x)
#print(k)
print(m)
# complex conversion is convert the all types of data
x = complex(i)
y = complex(f)
z = complex(b)
a = complex(c)
#x = complex(s1)
p = complex(s2)
l = complex(45)
m = complex(2,4)
print(x,y,z,a,p,l,m)
x = bool(i)
print(x)
u = bool(0+0j)
print(u)

