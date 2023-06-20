our_list = [4, 5, 1, 9, 0, 10]
sum = 0
for l in our_list:
    if l >= 5:   
        print (l)
    sum = sum + l
print (sum)

our_list2 = []
i = 0
while i < 10:
    our_list2.append(int(input('Enter a Number : ')))
    i = i + 1
print (our_list2)