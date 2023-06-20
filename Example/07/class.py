class Student:
    name = ''
    def score(self,x,y,z):
        s = (x + y + z) / 3
        return s

myStudent = Student()
myStudent.name = input('Enter Your Name : ')
print ('Hello ', myStudent.name)
result = myStudent.score(int(input('Please Enter Your First Score : ')),int(input('Please Enter Your Second Score : ')),int(input('Please Enter Your Third Score : ')))
print (result)