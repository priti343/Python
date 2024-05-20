import os
os.path.exists('D:\\Desktop\\Courses\\profiles-rest-api')
os.mkdir('C:\\ABC')
os.removedirs('C:\\GParent\\Parent\\Child')
os.rename('C:\\MYPython....')
os.rmdir('C:\\ABC')
os.getcwd()
os.makedirs('C:\\GParent\\Parent\\Child')
os.chdir('C:\\MyPython')
os.getlogin()


# CSV files
import csv
f = open('Employess.csv','r')
csv_reader=csv.reader(f)
print(csv_reader)