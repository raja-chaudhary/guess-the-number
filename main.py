from art import logo
# importing random module to generate a random number b/w 1-100
import random
import os                       # importing os to clear the screen before a new game


def play_game():
    print(logo)

    # generating a random number
    answer = random.randint(1, 100)
    game_difficulty = input("Select the game difficulty - easy/hard: ")

    # assigning attempts based on difficulty selected
    if game_difficulty.lower() == "easy":
        attempts = 10
        print("You will get 10 attempts to crack the answer!")
    else:
        attempts = 5
        print("You will get 5 attempts to crack the answer!")

    # repeat this logic till the user guesses or runs out of all attempts
    while attempts > 0:
        player_guess = int(input("Guess a number: "))
        if player_guess > answer:
            print("Too High!")
            attempts -= 1
            if attempts == 0:
                print("You Lose!!")
                print(f"The correct answer was {answer}.")
            else:
                print(f"You now have {attempts} attempts left!!")
        elif player_guess < answer:
            print("Too Low!")
            attempts -= 1
            if attempts == 0:
                print("You Lose!!")
                print(f"The correct answer was {answer}.")
            else:
                print(f"You now have {attempts} attempts left!!")
        else:
            print(f"You guessed it right, the answer is {answer}")
            attempts = 0

    # prompt to play again
    play_again = input("Would you like to play again - y/n? ")
    if play_again.lower() == 'y':
        os.system('clear')
        play_game()


play_game()
