import Student,pickle

studs=[Student.Student(10,'johan','cs'),Student.Student(20,'ajay','ec'),Student.Student(30,'khan','me')]
with open('Students.data','wb') as f:
    for S in studs:
        pickle.dump(S,f)