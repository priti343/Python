import csv
f = open('employees1.csv','r')
csv_reader=csv.reader(f)
print(csv_reader)
sals=[]
for row in csv_reader:
   # print(row[2])
     sals.append(int(row[2]))
print(sals)
print('Min' ,min(sals))
print('Max', max(sals))

