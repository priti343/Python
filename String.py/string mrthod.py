# see, everything in Python is an object.
#so string is also an object.
#string object will be automatically created from the class str.
#see a class will contain two things.one is data , the data that has to be stored
#and the second thing is it will contain operations and thus operations are nothing but functions.
s1 = 'hello, how are you'
print(type(s1))
dir(str)
print(dir(str))
#there are so many method.
dir(int)
print(dir(int))#there are so many method in int class.
print(help(s1.endswith))

#s.Find
s = 'hello,how are you'
print(s.find('o'))
print(s.find('how'))
print('k')
print(s.find('o',5))
print(s.find('o',5,7))
#s.rfind
print(s.rfind('o'))
print(s.rfind('o',0,15))
#s.index it is similar to s.find method
print(s.index('o'))
print(s.index('o',5))
 #print(s.index('k')) 


print(s.rindex('o',0,15))
str1='kadftycseauop'
ss = sorted(str1)
print(ss)
str2=''.join(ss)
print(str2)