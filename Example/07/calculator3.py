class Calculator:
    def Calculate(self,x,y,z):
        if z == '+':
            return x + y
        elif z == '-':
            return x - y
        elif z == '*':
            return x * y
        elif z == '/' and y != 0:
            return x / y
        else:
            return 'Not Valid Operation or Operator !!'

result = Calculator()
ave = result.Calculate (int(input('Enter Your First Number : ')),int(input('Enter Your Second Number : ')),input('Enter a Operator (+,-,*,/) : '))
print (ave)
while ave != 'Not Valid Operation or Operator !!':
    ave = result.Calculate (int(input('Enter Your First Number : ')),int(input('Enter Your Second Number : ')),input('Enter a Operator (+,-,*,/) : '))
    print (ave)