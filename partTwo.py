import random

def main():
    randNumber = random.randint(1,10)
    while True:
        guess = int(input('Guess a number between 1 and 10 > '))
        if checkGuess(guess, randNumber) == False:
            break
        else:
            continue
    
            
    
def checkGuess(guess, randNumber):
    if guess > randNumber:
        print ('Too high')
    elif guess < randNumber:
        print ('Too low')
    else:
        print ('Your guess is correct')
        return False
        
main()
    