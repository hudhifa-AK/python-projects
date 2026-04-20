import random

def random_number():
    random_number = [0,0,0]
    for i in range(3): #make three different random numbers
        random_number[i] = random.randint(0,9)
        while random_number[i] == random_number[i-1] or random_number[i] == random_number[i-2]:
            random_number[i] = random.randint(0,9)

    #convert to a string and return
    secret = ""
    for num in random_number:
        secret += str(num)
    print(secret)
    return secret

def get_guess():
    guess = input("Guess a 3 digit number: ")
    if len(guess) == 3 and guess.isdigit() == True: #get the guess from user but has to be 3 digits!
             return guess
    else:
        print("Invalid input. Try again with a 3 digit number")
        return get_guess() #loops back to ask again

def check_guess(guess, secret):
    score = ""
    for j in range(len(guess)): #compares each digit by the index
        if guess[j] == secret[j]:
            score += "Bullseye "
        elif guess[j] in secret:
            score += "Off-target "
        else:
            score += "Null "
    print(score) #prints the score for each digit

def play_game(): #main game function
    secret = random_number()
    attempt = 10
    while attempt != 0:
        guess = get_guess()
        check_guess(guess, secret)

        if guess == secret:
            print("You got it!")
            break

        attempt -= 1 #ten attempts are available each game

        if attempt == 0:
            print("You lost!")
            break

    return play_again() #asks the user play again?

def play_again():
    play_again = input("Do you want to play again? (y/n)")
    if play_again == "n":
        print("Thank you for playing!")
        return True #only way to leave the game is if the user inputs n
    elif play_again == "y":
        return play_game() #if y it calls the function play_game again
    else:
        print("Invalid input. Try again with a y or n")
        return False

play_game()
if play_again() == False:
    play_again()

# need to fix recursive function
