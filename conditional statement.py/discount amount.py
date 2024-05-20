amount = float(input("enter bill amount: "))

if amount <= 1000 :
    discount =  amount * 10 / 100
    print(discount)
elif amount>1000 and 5000>=amount:
    discount = amount*20/100
    print(discount)
elif amount>5000 and 10000>=amount:
    discount = amount*30/100
    print(discount)
else:
    discount = amount * 50/100
print(discount)
discount = amount - discount
print("pay",  discount) 
