def diff(n1,n2):
    if abs(n1-n2)<=5:
        return True
    else:
        return False
print(diff(15.4,12))

## maximum number in three
print('function : 3')
def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    elif c>a and c>b:
        return c
    else:
        return 0
print(max3(45,324,43)) 




## positional arguments
print('function: 4')


def massage(name, prof,/):
    print('My name is'+name+ ' and i am a/an ' +prof)
massage('Priti','Eng')

## find planet name by ID
print('function :5')
def planets(id):
    planet={1:'mercury', 2:'Venus',3:'Earth',4:'Mars',5:'Jupiter',6:'Saturn',7:'Uranus',8:'Neptune',9:'pluto'}
    return planet[id]
id = int(input('enter planet ID:'))
p = planets(id)
print('Planet Name is :',p)


# sum score ending with Zero
print('function : 6')
def sum0(L):
    s = 0
    for i in L:
        if i%10==0:
         s =s + i 
    return s
        
L=[200,342,400,2,532]

print(sum0(L))



# invert to dict
print('function : 7')
def invert(d):

    newd = {}
    for k, v in d.items():
        newd[v]=k
    return newd
d1= {'a':10, 'b':20, 'c':30, 'd':40}
d2 = invert(d1)

print((d2))   



#### pangram 
# 'the quick brown fox jumps over the lazy dog'

print('Function : 8')

def pangram(phrase):
    letters={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    phrase=set(phrase)
    if phrase>=letters:
        return(True)
    else:
          return(False)
print(pangram('The quick brown fox jumps over the lazy dog'))




## Case counting letters.
print('Function : 9')

def counts(phrase):
    lower=0
    upper=0
    for l in phrase:
        if l.islower():
           lower = lower+1  
     
        elif l.isupper():
            upper = upper+1
    return upper ,lower

print(counts('ABCdjgehp'))




## minimum variable number;
print('Function: 10')


def minimum(*value,low_limit=None):
    if low_limit is None:
        return min(value)
    else:
       l = [x for x in value if x>=low_limit]
    return min(l)
print(minimum(1,2,4,10,12,-56,20,25,low_limit=0))




### pascal's triangle
print('Function : 11')
def pascal(n):
    r=[1]


    for i in range(n):
        print(r)
        tep_r=[0]+r
        r=r+[0]
        r=[x+y for x,y in zip(r,tep_r)]
        
pascal(6)