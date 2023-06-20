x = int(input ('Enter First Number : '))
y = int(input ('Enter Second Number : '))
op = input ('Enter a Operator (+,-,*,/): ')
valid_operation = ['+','-','*','/']
if op in valid_operation:
    print ('Valid Operation')
else:    
    print ('Not a Valid Operation or Operator !!')