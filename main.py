import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

chosen_Number = random.randint(1, 100)


def player_choice():
    choice = (input("Type easy for Easy Mode or hard for Hard Mode: ")).lower()
    return choice


def game_loop(attempts):
    print(f"You have {attempts} to guess the number")
    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess != chosen_Number:
            attempts = attempts - 1
            if guess > chosen_Number:
                print("Too high")
                print("Guess again")
            else:
                print("Too low")
                print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number")
        else:
            print("You won !!!")
            break


if __name__ == '__main__':
    if player_choice() == "easy":
        game_loop(10)
    elif player_choice() == "hard":
        game_loop(5)
    else:
        player_choice()