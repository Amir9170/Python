x = int(input ('Enter First Number : '))
y = int(input ('Enter Second Number : '))
op = input ('Enter a Operator (+,-,*,/): ')
if op == '+':
    print (x+y)
elif op == '-':
    print (x-y)
elif op == '*':
    print (x*y)
elif op == '/' and y != 0:
    print (x/y)
else:
    print ('Not a Valid Operation or Operator !!')