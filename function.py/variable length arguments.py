# variable length arguments.py
def fun1(*args):#args means it is a variable arguments.it can  be change yourself.
    print(type(args),args)
fun1()
fun1(10,21)
fun1(10,20,30,40,50,60,70,80,90,100)
fun1(10,'hello',20.23,True)


# 
print('Function : 1')
def fun1(*args,a,b):
    print(a,b, args)
#fun1()
#fun1(11,22)
#fun1(11,22,33,44,55,66)
#fun1(a=11,b=22,33,44,55,66)# this is create error because its keyword writing left side.
fun1(11,22,33,44,a=55,b=66)


#Unpacking arguments 
print('function :2')

def fun2(a,b,c):
    print(a,b,c)

#L1 = [11,22,33]
#fun2(L1[0],L1[1],L1[2])
#print(*L1)
str1 = 'SKY'
fun2(*str1)

s1 = {23,45,55}
fun2(*s1)#we are using * convert the argument in unpack data.

##multiple return value;

print('Function :3')
def fun3(a,b,c):
    return a+1,b+1,c+1

print(fun3(10,30,40))
x,y,z=fun3(10,30,40)
print(x,y,z)

t = fun3(1,2,3)
print(t,type(t))


