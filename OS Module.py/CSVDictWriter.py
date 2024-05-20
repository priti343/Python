import csv

covid=[
{'Country':'India','Doses':'186Cr', 'People':'84.1Cr', 'Percentage':61},
{'Country':'China', 'Doses':'330Cr', 'People':'124Cr','Percentage':88.1},
{'Country':'United States','Doses':'56.8Cr', 'People':'21.9Cr', 'Percentage':66.4},
]

f = open('CSVDict.csv','w',newline='')

fileds=['Country','Doses','People','Percentage']

wrtr=csv.DictWriter(f,fileds)

wrtr.writeheader()
for d in covid:
    wrtr.writerow(d)

f.close()
