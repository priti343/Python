i = 0
   

#while i < 10:
  #  print(i,"hello")
 #   i = i+1
n = int(input('Enter the number:'))
while n > 0:
    r = n % 10
    n = n//10 # floor division
print(r)
