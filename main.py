# general idea: get three in a live with 2 players, 1 "X" and 1 "O"
# Text based grid
# if it works well, give option of computer

# TODO: make grid

# TODO give coordinates for placement

# TODO Check whether 3 in row or continue

# So far so good, now lets commit and continue on:

# TODO when all spaces are taken, finish game

# TODO ask to play again?
import random


pos = {}
for i in range(10):
    pos[i] = i

guessed = []

def print_grid():
    print(f"{pos[1]} | {pos[2]} | {pos[3]}")
    print("----------")
    print(f"{pos[4]} | {pos[5]} | {pos[6]}")
    print("----------")
    print(f"{pos[7]} | {pos[8]} | {pos[9]}")


def place_sign_x():
    choice = int(input("What position would you like to place the 'X'? "))
    if choice in guessed:
        print("That is already taken, try again.")
        return place_sign_x()

    guessed.append(choice)
    try:
        comp_choices.remove(choice)
    except ValueError:
        pass
    pos[choice] = "X"



def place_sign_o():
    choice = int(input("What position would you like to place the 'O'? "))
    if choice in guessed:
        print("That is already taken, try again.")
        return place_sign_o()
    guessed.append(choice)
    pos[choice] = "O"



def computer_place():
    comp_place = random.choice(comp_choices)
    pos[comp_place] = "O"
    guessed.append(comp_place)
    comp_choices.remove(comp_place)



def check_for_win():
    if pos[1] == pos[2] == pos[3]:
        print(f"Game over! {pos[1]} Wins!")
        return False
    elif pos[4] == pos[5] == pos[6]:
        print(f"Game over! {pos[4]} Wins!")
        return False
    elif pos[7] == pos[8] == pos[9]:
        print(f"Game over! {pos[1]} Wins!")
        return False
    elif pos[1] == pos[4] == pos[7]:
        print(f"Game over! {pos[1]} Wins!")
        return False
    elif pos[2] == pos[5] == pos[8]:
        print(f"Game over! {pos[2]} Wins!")
        return False
    elif pos[3] == pos[6] == pos[9]:
        print(f"Game over! {pos[3]} Wins!")
        return False
    elif pos[1] == pos[5] == pos[9]:
        print(f"Game over! {pos[1]} Wins!")
        return False
    elif pos[3] == pos[5] == pos[7]:
        print(f"Game over! {pos[3]} Wins!")
        return False
    elif len(guessed) == 9:
        print("Its a draw")
        return False


game_is_on = True

comp_choices = []
for i in range(1, 9):
    comp_choices.append(i)

game_mode = int(input("Type 1: vs player. Type 2: vs computer: "))


print_grid()

if game_mode == 1:
    while game_is_on:
        place_sign_x()
        print_grid()
        if check_for_win() == False:
            break


        place_sign_o()
        print_grid()
        if check_for_win() == False:
            game_is_on = False

elif game_mode == 2:
    while game_is_on:
        place_sign_x()
        if check_for_win() == False:
            break
        computer_place()
        if check_for_win() == False:
            break
        print_grid()
else:
    print("Invalid choice. Perhaps this game is too difficult for you.")