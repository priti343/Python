#s1 = 'decimal'
#s2 = 'medical'
s1 = input('Enter value: ')
s2 = input('Enter value: ')
if len(s1)!=len(s2):
    print('Not Anagram')
else:
    for x in s1:
        if x not in s2:
            print('Not anagram')
            break
    else:
            print('Anagram')


