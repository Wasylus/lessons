import random

# Repeat game 3 times (use for-loop and `range` function)
#   ask for input
#   generate computer move
#   decide who won this particular game
#   remember the winner (increase win counter by 1)

# check if counter of human player was equal to 2
# if yes, then print some message
# rock = "R"
# paper = "P"
# scissors = '''
# multi-line string
# hello
# hello
# '''

# escaped = 'quoted text: \'some quote\''

# text = "some quote"
# escaped = f"quoted text: \"{text}\""
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def martin():
    # if user wins at least 2 time, then he really wins
    # you need some memory for counting how many times human won (same for computer)
    player_win_counter = 0
    computer_win_counter = 0
    game_images = [ROCK, PAPER, SCISSORS]

    while True:
        print(f"HUMAN: {player_win_counter} | COMPUTER: {computer_win_counter}")

        if player_win_counter == 2:
            print("Human player has won")
            break
        if computer_win_counter == 2:
            print("Computer player has won")
            break

        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice >= 3 or user_choice < 0: 
            print("You typed an invalid number, you lose!") 
        elif user_choice == 0 and computer_choice == 2:
            print("You win!")
            player_win_counter += 1
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
            computer_win_counter += 1
        elif computer_choice > user_choice:
            print("You lose")
            computer_win_counter += 1
        elif user_choice > computer_choice:
            print("You win!")
            player_win_counter += 1
        elif computer_choice == user_choice:
            print("It's a draw")
            # noone gets a point
            # computer_win_counter += 1
            # player_win_counter += 1


ROCK_ID = 0
PAPER_ID = 1 
SCISSORS_ID = 2
GAME_IMAGES = [ROCK, PAPER, SCISSORS]

def ask_for_input():
    return int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

def miczi():
    player_win_counter = 0
    computer_win_counter = 0
    NUM_AVAILABLE_ACTIONS = len(GAME_IMAGES)
    WINNING_SCORE = 2

    while True:
        print(f"HUMAN: {player_win_counter} | COMPUTER: {computer_win_counter}")

        if player_win_counter == WINNING_SCORE:
            print("Human player has won")
            # exit while loop
            break
        if computer_win_counter == WINNING_SCORE:
            print("Computer player has won")
            # exit while loop
            break

        user_choice = ask_for_input()

        # input validation
        if user_choice >= NUM_AVAILABLE_ACTIONS or user_choice < 0: 
            print("You typed an invalid number, you lose!") 
            # skip this loop iteration, force him to try again
            continue

        computer_choice = random.randrange(len(GAME_IMAGES)) # <0; 2> = 0, 1, 2

        display_player(user_choice, "Human")
        display_player(computer_choice, "Computer")

        player_won = has_player_won(user_choice, computer_choice)
        if player_won:
            player_win_counter += 1
        else:
            computer_win_counter += 1

def display_player(img_index: int, player_name: str):
    print(f"{player_name} chose:")
    print(GAME_IMAGES[img_index])

def has_player_won(user_choice, computer_choice):
    if user_choice == ROCK_ID and computer_choice == SCISSORS_ID:
        return True
    elif computer_choice == ROCK_ID and user_choice == SCISSORS_ID:
        return False
    elif computer_choice > user_choice:
        return False
    elif user_choice > computer_choice:
        return True
    elif computer_choice == user_choice:
        # it's a draw
        return None
    
miczi()



print("THE END")
# END OF EXECUTION

# Function order matters (but not always)
# Explanation: https://stackoverflow.com/questions/44423786/does-the-order-of-functions-in-a-python-script-matter
# def print_sum(a, b):
#     print(sum_numbers(a, b))

# print_sum(2, 4)

# def sum_numbers(a, b):
#     return a + b