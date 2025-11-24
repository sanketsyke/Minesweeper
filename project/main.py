from board import Board
from game_logic import check_win, check_loss
from file_manager import save_game, load_game

# Get user input for action: reveal (r), flag (f), save (s), or quit (q)
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
            board = Board()   # Start a new game with fresh board
            rng_seed = None   # Use a random seed for mine placement
            break
        elif choice == 2:
            board, rng_seed = load_game()  # Load previously saved game
            if board is None:
                print("No saved game found. Starting new game.")
                board = Board()
            else:
                print("Loaded saved game.")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

    # Main game loop: runs until player wins, loses, or quits
    while True:
        board.display()  # Show current board state

        if check_win(board):  # Check for win condition
            print("CONGRATULATIONS! You cleared all non-mine cells.")
            print("You WIN!! 🎉🎉")
            break

        action = get_player_action()  # Get player input
        if not action:
            continue

        if action[0] == 'q':  # Quit game
            print("Quitting game.")
            break

        elif action[0] == 's':  # Save current game state
            save_game(board, rng_seed)
            print("Game saved.")
            continue

        elif action[0] in ('r', 'f') and len(action) == 3:  # Reveal or flag cell
            row = int(action[1]) - 1  # Convert to 0-based index
            col = int(action[2]) - 1
            if action[0] == 'r':
                board.reveal(row, col)
                if check_loss(board):  # Check if revealed mine (loss condition)
                    board.display(reveal_all=True)  # Show full board with mines
                    print("Game Over! 💀💀 You hit a mine.")
                    break
            elif action[0] == 'f':
                board.toggle_flag(row, col)
        else:
            print("Invalid action.")

if __name__ == '__main__':
    main()
