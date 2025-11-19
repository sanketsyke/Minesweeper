# Importing class Board from board.py
from board import Board

# Importing functions check_win and check_loss from game_logic.py
from game_logic import check_win, check_loss

# Importing functions save_game and load_game from file_manager.py
from file_manager import save_game, load_game


# get_player_action is used to take input from user regarding the action
#               the user wants to perform 
def get_player_action():
    action = input("Enter action (r row col for reveal, f row col for flag, s to save, q to quit): ").strip().split()
    return action

def main():
    print("""                                                                     
                                                                     
██▄  ▄██ ▄▄ ▄▄  ▄▄ ▄▄▄▄▄  ▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄  
██ ▀▀ ██ ██ ███▄██ ██▄▄  ███▄▄ ██ ▄ ██ ██▄▄  ██▄▄  ██▄█▀ ██▄▄  ██▄█▄ 
██    ██ ██ ██ ▀██ ██▄▄▄ ▄▄██▀  ▀█▀█▀  ██▄▄▄ ██▄▄▄ ██    ██▄▄▄ ██ ██ 
                                                                     """)
    while True:
        choice = int(input("1. New Game\n2. Load Game\nChoose (1/2): "))

        if choice == 1:
            board = Board()   # Creates a new board
            rng_seed = None   # Random mine layout
            break
        elif choice == 2:
            board, rng_seed = load_game()  # Loading the previous game
            if board is None:
                print("No saved game found. Starting new game.")
                board = Board()
            else:
                print("Loaded saved game.")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

    # Main Game Loop: runs until win, loss or quit.
    while True:
        board.display()                # Prints current board
        if check_win(board):           # Check if player won
            print("CONGRATULATOINS! You cleared all non-mine cells.")
            print("You WIN!! 🎉🎉")
            break
        action = get_player_action()   # Take player action (r row col, f row col, s, q)
        if not action:                 
            continue

        # Quitting game
        if action[0] == 'q':
            print("Quitting game.")
            break

        # Saving game
        elif action[0] == 's':
            save_game(board, rng_seed)
            print("Game saved.")
            continue

        # Reveal or Flag cell
        elif action[0] in ('r', 'f') and len(action) == 3:
            row = int(action[1]) - 1       # Converts the second and third character of the string to int
            col = int(action[2]) - 1       # representing row and column and -1 is to convert 1-based index to 0-based
            # Revealing
            if action[0] == 'r':
                board.reveal(row, col)
                # Checking if the player hit a mine
                if check_loss(board):
                    board.display(reveal_all=True)
                    print("Game Over! 💀💀 You hit a mine.")
                    break
            # Flagging and unflagging
            elif action[0] == 'f':
                board.toggle_flag(row, col)
        else:
            print("Invalid action.")

# This part is used to run the file only when executed directly and not while importing main
if __name__ == '__main__':
    main()
