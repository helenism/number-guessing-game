import random

random_number = random.randint(1,10)
random_number = str(random_number)
#print random_number #Uncomment to quickly test if game works by having the printed random number.

you_win = False

while you_win == False:
    guess = raw_input('Guess a number between 1 and 10:')
    if guess == random_number:
        you_win = True

if you_win == True:
    print 'YOU WIN!'
