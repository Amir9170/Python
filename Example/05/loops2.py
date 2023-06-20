j = 0
count = 0
sum = 0
while j != '':
    j = input('Enter a number (Left Blank to Calculate) : ')
#    if j != '':
#        sum = sum + int(j)
#        count = count + 1
    if j == '':
        continue
    sum = sum + int(j)
    count = count + 1

print (sum / count)