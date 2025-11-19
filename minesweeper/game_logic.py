# Function to check whether the player has won
def check_win(board):
    for row in board.grid:      # Iterate over each row in the grid
        for cell in row:        # Iterate over each cell in current row
            if not cell.mine and not cell.revealed:     # If a cell is not a mine and is still hidden then the player has not won yet
                return False
    return True                 # If every cell which is not a mine is revealed, then the player wins

#Function to check whether the player has lost
def check_loss(board):
    for row in board.grid:      # Iterate over each row in the grid
        for cell in row:        # Iterate over each cell in current row
            if cell.mine and cell.revealed:     # If a cell is a mine and revealed, then the player has lost
                return True
    return False                # If no revealed mines are found, the player hasn't lost
