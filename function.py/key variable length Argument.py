# keyword,variable length arguments 
print('Function :1')
def fun2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for x in kwargs:
        print(x, kwargs[x])
fun2(name='rohan',roll=100, addr='Delhi')

# mixed arguments
print('Function :3')
def fun3(a,b,*arags,c,**kwarags):
    print(a,b,arags,c,kwarags)
    print(type(arags))
    print(type(kwarags))
    print(type(fun3))

fun3(2,3, 46,74,88,c=5,name='Mohan',age=45,add='lucknow')
print(fun3)