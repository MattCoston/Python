import random

def game():
#generate random number
    secret_num = random.randint(1, 10)
    guesses = [] 

    while len(guesses) < 5:
            try:
                    guess = int(input("You have 5 tries.  Guess a number between 1 and 10: "))
            except ValueError:
                    print("{} THAT'S NOT A NUMBER!!!".format(guess))
# give feedback on number guess depending on how high or low
            if guess == secret_num:
                    print("CORRECT!")
                    print("END")
                    break
            elif guess < secret_num:
                    print("TOO LOW")
                    guesses.append(guess)
            elif guess > secret_num:
                    print("TOO HIGH")
                    guesses.append(guess)
    else:
        print("The number was: " + str(secret_num))
    play_again = input("play again Y/n? ")
    if play_again.lower() != 'n':
        game()
    else:
        print("BYE")
        
game()
