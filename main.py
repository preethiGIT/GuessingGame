import random

big=32
guesses=5

name=input('what is your name? ')
print('Hi {0}'.format(name))

level=1
flag=True

while flag==True:
    number=random.randint(1,big)
    print('I am thinking of a  number between 1 and {0} {1}, guess my number. '.format(big, number))
    print('Random: {0}'.format(number))
    for i in range(guesses):
        guess=int(input('guess'))
        if guess > big:
            print('pick a number less than or equal to {0}'.format(big))
        elif guess < number:
            print('your guess is too small')
        elif guess > number:
            print('your guess is too big')
        elif guess==number:
            print('good job, it only took you {0} guesses.'.format(i+1))
            ans=input('press 1 to continue same level,2 to level up and 3 to quit ')
            if ans == '1':
                break
            elif ans =='2':
                level=level+1;
                print('You choose to level up!!Welcome to level {0}'.format(level))
                big*=2
                break
            elif ans =='3':
                flag=False
                break
                
    else:
        print('sorry, you lost my number was {0} try harder next time'.format(number))
