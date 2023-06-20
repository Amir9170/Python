from libs.AvgCalculator import AvgCalculator
import random

# n = random.random()
# print (n)

# m = random.randint(0,22)
# m = random.randrange(100)
# print (m)

x = int(input('Please Enter Riazyi Score : '))
y = int(input('Please Enter Fizik Score : '))
z = int(input('Please Enter Shimi Score : '))
ac_class = AvgCalculator()
mean = ac_class.calculate(x,y,z)
print (mean)