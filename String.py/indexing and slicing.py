'''s2 = 'helloworld'
len(s2)
for x in range(0,len(s2)):
    print(s2[x])'''
#reverse string 
s2 = 'Helloworld'
for i in range(len(s2)-1,-1,-1):
    print(s2[i])
# every second character skipped and taken i again;
for i in range(0,len(s2),2):

    print(s2[i])
s1 = 'Hello World'
s1[0:len(s1):1]
print(s1)
s1[:len(s1):1]
print(s1)
s1[::1]
print(s1)
s1[::]
print(s1)
s1=s1[3::]
print(s1)
s1 = s1[6::]
print(s1)
s2 = 'HELLO WORLD'
s2 = s2[::3] 
print(s2)
#reverse string
s3 = 'Hello world'
s3 = s3[::-1]
print(s3)
s3 = s3[-1::-1]
print(s3)
s3 = s3[-1::-1] #reverse string
print(s3)
s3 = s3[-1::]
print(s3)