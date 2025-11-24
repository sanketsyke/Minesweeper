# Check if the player has won by revealing all non-mine cells
def check_win(board):
    for row in board.grid:
        for cell in row:
            if not cell.mine and not cell.revealed:
                return False  # Unrevealed non-mine cell means game not won yet
    return True  # All non-mine cells revealed, player wins

# Check if the player has lost by revealing any mine cell
def check_loss(board):
    for row in board.grid:
        for cell in row:
            if cell.mine and cell.revealed:
                return True  # Revealed mine means game lost
    return False  # No revealed mines, player hasn't lost
