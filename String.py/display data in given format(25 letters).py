item = input('Enter the Item: ')
price= input('Enter price: ')
total_len = len(item)+len(price)
print(total_len)
dots = '.'*(25-total_len)#'.'is represent multiple dots
print(item+dots+price)#dots print in between
print(item+price+dots)#dots prints in last
