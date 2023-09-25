import os
# general idea: get three in a live with 2 players, 1 "X" and 1 "O"
# Text based grid
# if it works well, give option of computer

# TODO: make grid

# TODO give coordinates for placement

# TODO Check whether 3 in row or continue

game_is_on = True

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
    pos[choice] = "X"
    print_grid()

def place_sign_o():
    choice = int(input("What position would you like to place the 'O'? "))
    if choice in guessed:
        print("That is already taken, try again.")
        return place_sign_o()
    guessed.append(choice)
    pos[choice] = "O"
    print_grid()

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


print_grid()
while game_is_on:
    place_sign_x()
    if check_for_win() == False:
        game_is_on = False

    place_sign_o()
    if check_for_win() == False:
        game_is_on = False

