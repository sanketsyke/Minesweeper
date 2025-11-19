# Import os module for filesystem utilities
import os

# Import pickle for serializing python objects to a file 
import pickle

# Importing class Board from board.py
from board import Board

# Path where the saved data is to be written
SAVE_FILE = 'data/minesweeper_save.txt'

# Function to save the current game state
def save_game(board, rng_seed):
    # Building a dictionary that captures the state of the board
    state = {
        'rows': board.rows,
        'cols': board.cols,
        'mines': board.mines,
        'flags_left': board.flags_left,
        'rng_seed': board.rng_seed,
        # nested list comprehension to serialise each cell as a dict
        'cells': [[{
            'mine': cell.mine,
            'revealed': cell.revealed,
            'flagged': cell.flagged,
            'adjacent': cell.adjacent
        } for cell in row] for row in board.grid]
    }
    # open the save file in binary write mode
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(state, f)     #write the state dict to disk using pickle 

# Function to load a saved game
def load_game():
    if not os.path.exists(SAVE_FILE):   # check whether the save file exists
        return None, None               # if the save file doesnt exist, returns a pair of Nones indicating nothing loaded
    with open(SAVE_FILE, 'rb') as f:    # opens the save file in binary read mode
        state = pickle.load(f)          # reads the stored state dict from disk
    # Restoring the saved Board with the saved dimensions and seed
    board = Board(rows=state['rows'], cols=state['cols'], mines=state['mines'], rng_seed=state['rng_seed'])
    for r in range(board.rows):
        for c in range(board.cols):
            cell_data = state['cells'][r][c]   # using the saved dict for this cell
            cell = board.grid[r][c]            # get the matching cell object
            # Assign saved data onto the cell to match the saved board
            cell.mine= cell_data['mine']
            cell.revealed = cell_data['revealed']
            cell.flagged  = cell_data['flagged']
            cell.adjacent = cell_data['adjacent']
    return board, state['rng_seed']            # Return the saved board and stored seed
