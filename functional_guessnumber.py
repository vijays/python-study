import random

def process_guess(num, guess):
    if 0 < guess < 11:
        if guess == num:
            print('You guessed it!')
            return True
        else:
            return False
    else:
        print('Enter between 1 to 10')
        return False


if __name__ == '__main__':
    
    # generate random number
    num = random.randint(1, 10)    
    
    while True:
        guess =  int(input('Guess Number: '))   
    
        if (process_guess(num, guess)):
            break
        else:
            continue
    

    