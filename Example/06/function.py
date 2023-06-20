customers = {'09125226365':'Hamed Lahijani',
             '09121029940':'Yaghoub Rasoulzadeh',
             '09124216383':'Amir Rasoulzadeh',
             '09124112684':'Omid Rasoulzadeh'}
i = input('Please Enter a Phone Number : ')
while i != '':
    if not i in customers:
        customers[i] = input('Enter Your Firstname and Lastname : ')
        print (customers[i], ', Add to Customer List !!')
    else:
        print (customers[i],', Available in the list')
    i = input('Please Enter a Phone Number : ')
#print (customers)