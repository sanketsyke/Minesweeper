import os
import pickle
from board import Board

SAVE_FILE = 'data/minesweeper_save.txt'  # File path for saving game state

def save_game(board, rng_seed):
    # Build a serializable dictionary capturing the entire board state
    state = {
        'rows': board.rows,
        'cols': board.cols,
        'mines': board.mines,
        'flags_left': board.flags_left,
        'rng_seed': rng_seed,
        'cells': [[{
            'mine': cell.mine,
            'revealed': cell.revealed,
            'flagged': cell.flagged,
            'adjacent': cell.adjacent
        } for cell in row] for row in board.grid]
    }
    # Serialize the state dictionary to a file in binary mode
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(state, f)

def load_game():
    # Return None if no saved file exists
    if not os.path.exists(SAVE_FILE):
        return None, None
    # Load the saved state dictionary from file
    with open(SAVE_FILE, 'rb') as f:
        state = pickle.load(f)
    # Reconstruct Board instance with saved settings
    board = Board(rows=state['rows'], cols=state['cols'], mines=state['mines'], rng_seed=state['rng_seed'])
    # Restore cell properties from saved data
    for r in range(board.rows):
        for c in range(board.cols):
            cell_data = state['cells'][r][c]
            cell = board.grid[r][c]
            cell.mine = cell_data['mine']
            cell.revealed = cell_data['revealed']
            cell.flagged = cell_data['flagged']
            cell.adjacent = cell_data['adjacent']
    return board, state['rng_seed']
