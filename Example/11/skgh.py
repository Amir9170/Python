# from random import randint
from random import choice

player_score = 0
computer_score = 0

game = {
    's': 'Sang',
    'k': 'Kaghaz',
    'g': 'Gheychi'
}
while True:
    choices = ['s','k','g']
    i = input('Sang(s), Kaghaz(k), Gheychi(g): ')
    if i not in choices:
        print ('Not a Valid Input!')
        continue
    print ('You Choose ' + game[i])
    c = choice(choices)
#    random_number = randint(0,2)
#    c = choices[random_number]
    print ('Computer Choose ' + game[c])
    if i == c:
        print ('Mosavvi Shod!')
    elif i == 's':
        if c == 'k':
            print ('Computer Wins!')
            computer_score += 1
        else:
            print ('You Wins!')
            player_score += 1
    elif i == 'k':
        if c == 's':
            print ('You Wins!')
            player_score += 1
        else:
            print ('Computer Wins!')
            computer_score += 1
    else:
        if c == 's':
            print ('Computer Wins!')
            computer_score += 1
        else:
            print ('You Wins!')
            player_score += 1
    print ('+++++++++++++++++++')
    print ('Your Scores =' + str(player_score))
    print ('Computer Scores =' + str(computer_score))
    print ('+++++++++++++++++++')
    t = input('Continue? (y/n) : ')
    if t == 'n':
        break
    elif t == 'y':
        continue