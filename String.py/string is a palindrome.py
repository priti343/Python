# checking a string is a palindrome
s1 = 'madam'
rev = s1[::-1]
if s1 == rev:
    print('Palindrome')
else:
    print('not palindrome')
#converting string to palindrome 
s2 = input('enter a string: ')
rev = s2[::-1]
rev2 = s2 + rev
print(rev2)
rev3 = rev2[::-1]
if rev2==rev3:
    print('It is palindrome')
else:
    print("it's not palindrome")

