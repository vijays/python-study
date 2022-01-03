import random

# generate random number
num = random.randint(1, 10)


while True:
    guess =  int(input('Guess Number: '))   

    if 0 < guess < 11:
        if guess == num:
            print('You guess it!')
            break
        else:
            continue
    else:
        print('Enter between 1 to 10')