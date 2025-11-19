#Importing Python's random module for placing mines
import random

#Defining a cell
class Cell:   
    #Initialising the Board
    def __init__(self, mine=False):
        self.mine = mine
        self.revealed = False
        self.flagged = False
        self.adjacent = 0

    #Cell Display
    def __str__(self):    
        if self.flagged:
            return '🚩'
        if not self.revealed:
            return '.'
        if self.mine:
            return '💥'
        if self.adjacent == 0:
            return ' '
        return str(self.adjacent)

# Defining Board
class Board:
    #Initialises the grid
    def __init__(self, rows=9, cols=9, mines=10, rng_seed=None, state=None):
        #If the user chooses Load game    
        if state:
            self.__dict__.update(state)     #restores board directly from that saved dict

        #Otherwise a new board is created
        else:
            # Random seed generator to generate different mine layouts
            if rng_seed is not None:
                random.seed(rng_seed)
                self.rng_seed = rng_seed
            else:
                self.rng_seed = random.randint(0, 999999)
                random.seed(self.rng_seed)
            # Initialising the game grid
            self.rows = rows
            self.cols = cols
            self.mines = mines
            self.flags_left = mines
            self.grid = [[Cell() for i in range(cols)] for j in range(rows)]
            self.place_mines()
            self.calculate_adjacency()

    # Places mines randomly
    def place_mines(self):
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        mine_cells = random.sample(all_cells, self.mines)    # Picks unique mine locations
        for r, c in mine_cells:
            self.grid[r][c].mine = True     # Marking those cells as mines

    # Calculates number of mines adjacent to a non-mine cell
    def calculate_adjacency(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].mine:  #Skipping mines
                    continue
                # Counting the number of neighbouring cells with mines
                count = sum(
                    self.grid[nr][nc].mine
                    # Iterating over the neighbouring cells
                    for nr in range(max(0, r-1), min(self.rows, r+2))  
                    for nc in range(max(0, c-1), min(self.cols, c+2))
                    if not (nr == r and nc == c)
                )
                self.grid[r][c].adjacent = count
    
    #Reveals a cell and flood-fills if it is empty
    def reveal(self, row, col):
        cell = self.grid[row][col]              # Target cell
        if cell.revealed or cell.flagged:       # If already revealed or flagged do nothing
            return
        cell.revealed = True
        if cell.mine or cell.adjacent > 0:      # Mark the cell revealed if its a mine or has adjacent mines
            return                              # NO flood-fill   
        # Flood Fill i.e if we choose to reveal a cell with no mines around it
        # it recursively reveals the neighbours until we reach a cell with a mine around it
        for nr in range(max(0, row-1), min(self.rows, row+2)):
            for nc in range(max(0, col-1), min(self.cols, col+2)):
                if not (nr == row and nc == col):
                    self.reveal(nr, nc)

    #Place or remove a flag
    def toggle_flag(self, row, col):
        cell = self.grid[row][col]                      #Target cell
        if cell.revealed: 
            return                                      #Cannot flag a revealed cell
        cell.flagged = not cell.flagged                 #Toggles the flag
        self.flags_left += -1 if cell.flagged else 1    #Decrement flags_left when flag placed and increment when flag removed 

    #Display of the board
    def display(self, reveal_all=False):
        cell_width = 2         #Width for each cell
        print("    ", end="")  # 4 spaces for the row label and separator
        for c in range(self.cols):
            print("",c+1, end=" ")   # Column index
        print("\n     _  _  _  _  _  _  _  _  _")
        for r in range(self.rows):
            print(r+1," |", end="")  # Row index
            for c in range(self.cols):
                if reveal_all:       # Showing full board
                    if self.grid[r][c].mine: ch = '💥'
                    else:
                        if self.grid[r][c].adjacent > 0: ch = str(self.grid[r][c].adjacent)
                        else: ch = ' '
                else:
                    ch = str(self.grid[r][c])
                print(f" {ch}", end=" ")
            print()
        print(f"Flags left: {self.flags_left}")


