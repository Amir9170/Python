from random import randrange
number = randrange(0,100)
has_guesses = False

while has_guesses == False:
    i = int(input('Enter a Number : '))
    if i == number:
        print ('OK! The Number is ' + str(i))
        has_guesses = True
    elif i > number:
        print ('Your Guess in High')
    elif i < number:
        print ('Your Guess is Low')