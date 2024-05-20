file = open('file.txt','r')
str1=file.read()
print(str1)
file = open('file.txt','w')
file.write('How are you. \n')
file.write('hello\n')
file.write('do you known python')
file.close()



#properties of file
#f.name
#f.mode
#f.closed
