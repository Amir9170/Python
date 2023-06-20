i = (3, 4, 5, 'masoud')
print (i[0])

my_list = [4 , 'masoud' , 'kaviani' , 8]
my_list2 = [5 , 10]
my_list.extend(my_list2)
my_list.append(15)
print (my_list)
i = my_list.pop()
print (i)
print (my_list)

dic = {'Amir':19 , 'Omid':20 , 'Zahra':18.5}
print (dic['Amir'])
dic['Amir'] = 20
print (dic['Amir'])