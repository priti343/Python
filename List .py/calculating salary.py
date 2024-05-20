work_hours = [int(x) for x in input('Enter hours per day in etire week, separated by space: ').split()]
wage = int(input('Enter hourly wage'))
total = sum(work_hours)
salary= total*wage
print(sum(work_hours))
print('Salary is ',salary)

