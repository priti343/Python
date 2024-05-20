n = int(input('Enter a Number :'))
#m = n
rev = 0
while n > 0:
    r = n%10
    n = n//10
    rev = rev * 10 +r
#if m==rev:
        #print('program is palindrone')
#else:
        #print('program is not palindrone')
print('Reverse number is', rev)