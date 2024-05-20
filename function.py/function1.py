def add3(a,b,c):
    r = a+b+c
    return r #if u are writing in there so it's return none.
print(add3(3,4,6))# fist given the value 
return_value=add3(3,4,6)
print(return_value)#second value given this statment.
print('function 2:')
def add3(a,b,c):
    print('inside function', id(a), id(b), id(c))


x, y,z=10,22,11 
print('outside function', id(x),id(y),id(z)) 
print(add3(x,y,z))



print('function 3:')


def net_sal(basic,allowance,deduction):
    
    print('basic',basic)
    print('allowance', allowance)
    print('deduction',deduction)
    net = basic + allowance -deduction
    return net

#n = net_sal(8000,6000,2000)
#print('Net Salary is : ', n)
n = net_sal (deduction=2000,basic = 8000,allowance=6000)
print('Net salary is :',n)

#default arguments;;-----
print('function :4')

def add(a,b=0,c=0):
    return a+b+c


print(add(43,8,9))
print(add(8))


# additem in list
print('function :5')


def addItem(item, L=[]):
          L.append(item)
          return L
L1=[2,3,4,5]
addItem(7,L1)
print(L1)
addItem(99,L1)# this means defaults are created only one.
print(L1)
print(addItem(44))
print(addItem(54))
print(addItem(87))
print(addItem(22))
print(addItem(49))

### Mixed Positional or keyword Argument
print("function :6")
def add(a,b,c,d,e,f):
     return a+b+c+d+e+f
print(add (2,3,5,6,7,8)) # this positional arguments
print(add(f=8,c=4,b=4,d=9,e=10,a=12)) # keyworld arguments.



# mixed positional or keyword arguments
print('function :7')
def add(a,b,/,c,d,e,f):# there are a and b is mandatory positional.
     return a+b+c+d+e+f

print(add(8,4,c=34,e=5,d=9,f=33))## Mixed positional or keyword arguments.

print('function :8')
def add(a,b,/,c,d,*,e,f):#there are a and b is mandatory positional and c and d is any type and e or f is only keyword arguments.
     
     return a+b+c+d+e+f
r = add(9,8,c=10,d=11,e=44,f=14)
print(r)



