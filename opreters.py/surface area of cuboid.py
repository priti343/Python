#Total surface area of cuboid
#6 side
#front and back =  2(l*h)
#bottom and top = 2(length*breath)
#letf and right = 2(breath*height)
#total = 2(lh+lb+bh)
lenght = int(input('Enter length: '))
breath = int(input('Enter breath: '))
height = int(input('Enter height: '))
area = 2*(lenght*height+breath*lenght+breath*height)
print("Total surface area is", area)
