Year = int(input("enter year: "))
if Year % 100 == 0:
   if Year % 400==0:
    print('Leap year')
   else:
    print('not leap year ')
elif Year % 4 == 0 :
  print('leap year')
else:
  print('Not leap year')
 
