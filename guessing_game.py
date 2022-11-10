# guessing game

from random import randint

from IPython.display import clear_output

guessed = False
number = randint(0, 100)
guesses = 0

while not guessed:
    try:
        ans = int(input("Try to guess the number I am thinking of!: "))
    except:
        print("That's not a valid option!")
    # use tab to indent
    guesses += 1
    clear_output()
    
    if int(ans) == number:
        print("Congrats! You guessed it correctly. ")
        if int(ans) != int:
            print("Invalid Entry. Please enter an Integer between 1 and 100: ")
        # use tab twice to indent twice
        print("It took you {} guesses!".format(guesses))
        break
        
    elif int(ans) > number:
        print("The number is lower than you guessed. ")
        if int(ans) > 100:
            print("You are out of bounds!")
    elif int(ans) > number + 5 or - 5:
        print("You are geting close! ") 
        
    elif int(ans) < number:
        print("The number is greater than you guessed. ")
        
    elif str(int(ans)) != number:
        print("Invalid Entry. Please enter an Integer between 1 and 100: ")
        