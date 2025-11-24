import random

# Minesweeper game board and cell logic

class Cell:  
    def __init__(self, mine=False):
        self.mine = mine
        self.revealed = False
        self.flagged = False
        self.adjacent = 0

    def __str__(self):    
        if self.flagged:
            return '🚩'
        if not self.revealed:
            return '.'
        if self.mine:
            return '💥'
        if self.adjacent == 0:
            return ' '
        return str(self.adjacent)  # Display number of adjacent mines as a string


class Board:
    def __init__(self, rows=9, cols=9, mines=10, rng_seed=None, state=None):
        if state:
            self.__dict__.update(state)  # Load saved game state
        else:
            if rng_seed is not None:
                random.seed(rng_seed)
                self.rng_seed = rng_seed
            else:
                self.rng_seed = random.randint(0, 999999)
                random.seed(self.rng_seed)
            self.rows = rows
            self.cols = cols
            self.mines = mines
            self.flags_left = mines
            self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
            self.place_mines()
            self.calculate_adjacency()

    def place_mines(self):
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        mine_cells = random.sample(all_cells, self.mines)
        for r, c in mine_cells:
            self.grid[r][c].mine = True

    def calculate_adjacency(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].mine:
                    continue
                count = sum(
                    self.grid[nr][nc].mine
                    for nr in range(max(0, r-1), min(self.rows, r+2))
                    for nc in range(max(0, c-1), min(self.cols, c+2))
                    if not (nr == r and nc == c)
                )
                self.grid[r][c].adjacent = count
    
    def reveal(self, row, col):
        cell = self.grid[row][col]
        if cell.revealed or cell.flagged:
            return
        cell.revealed = True
        if cell.mine or cell.adjacent > 0:
            return 
        # Flood fill reveal for empty cells with no adjacent mines
        for nr in range(max(0, row-1), min(self.rows, row+2)):
            for nc in range(max(0, col-1), min(self.cols, col+2)):
                if not (nr == row and nc == col):
                    self.reveal(nr, nc)

    def toggle_flag(self, row, col):
        cell = self.grid[row][col]
        if cell.revealed:
            return  # Cannot flag already revealed cell
        cell.flagged = not cell.flagged
        if cell.flagged:
            self.flags_left -= 1
        else:
            self.flags_left += 1

    def display(self, reveal_all=False):
        cell_width = 2         
        print("    ", end="")  
        for c in range(self.cols):
            print("",c+1, end=" ")   
        print("\n     _  _  _  _  _  _  _  _  _")
        for r in range(self.rows):
            print(r+1," |", end="")  
            for c in range(self.cols):
                if reveal_all:       
                    if self.grid[r][c].mine: ch = '💥'
                    else:
                        if self.grid[r][c].adjacent > 0: ch = str(self.grid[r][c].adjacent)
                        else: ch = ' '
                else:
                    ch = str(self.grid[r][c])
                print(f" {ch}", end=" ")
            print()
        print(f"Flags left: {self.flags_left}")
