pass1 = input('enter password: ')
pass2 = input('confirm password: ')
if pass1==pass2:
    print('Succussefully!')
else:
    if pass1.casefold()==pass2.casefold():
        print('Please check for the cases and try again')
    else:
        print('No they are not matching try them again')