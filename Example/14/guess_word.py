import sys

name = input('Please Enter Your Name : ')
print ('Hello, ' + str(name))
word = 'chistio.ir'
turn = 10
guess = ''
while turn > 0:
    i = input('Enter a Character : ')
    
    if len(i) != 1:
        print ('Please Enter Exactly "ONE" Character!')
        continue
    
    guess = guess + i
    if i not in word:
        turn = turn - 1
        print ('Wrong!')
        print ('You have ' + str(turn) + ' Turn')   
    
    win = True
    for c in word:
        if c in guess:
            sys.stdout.write (c)
        else:
            sys.stdout.write ('_')
            win = False
    
    if win == True:
        print ('\nCongratulations, You Win The Game !!')
        break

if win == False:
    print ('\nYou Loose The Game !!')