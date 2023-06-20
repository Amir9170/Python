def user_input():
    x = input('Please Enter a Pharse: ')
    return x

def acronym(pharse):
    y = pharse.split()
    z =[]
    for word in y:
        if len(word)<=2:
            continue
        z.append(word[0])
    u = ''.join(z)
    return u

ui = user_input()
a = acronym(ui)
print (a)