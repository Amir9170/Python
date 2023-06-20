def serch_customer(x):
    customers = {'09125226365':'Hamed Lahijani',
             '09121029940':'Yaghoub Rasoulzadeh',
             '09124216383':'Amir Rasoulzadeh',
             '09124112684':'Omid Rasoulzadeh'}
    if x in customers:
        return True
    else:
        return False

i = input('Please Enter a Phone Number : ')
while i != '':
    result = serch_customer(i)
    if result:
        print ('Yes, The Customer Exists!')
    else:
        print ('No, The Customer does not Exists !')
    i = input('Please Enter a Phone Number : ')