from random import randint

number = randint(0,100)
while True:
    guess = int(input('Please Enter Your Guess :'))
    if guess != number:
        if guess > number:
            print('Your Guess is High')
        elif guess < number:
            print('Your Guess is Low')
    else:
        break
print ('Your Guess is True, You Win !!')