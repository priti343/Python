import csv

import pprint


f = open('employees1.csv','r')
rdr=csv.DictReader(f)
emps={}
for row in rdr:

    emps[row['Name']]=row


    #print(row)

pprint.pprint(emps)
print('Harry',emps['Harry'])

f.close()
