# Minesweeper CLI

## Project Overview
This project is a classic Minesweeper game in a CLI (Command Line Interface). It features a fully functional game board with mines placed randomly, flagging, revealing cells, saving and loading the previously saved game.

## Features
- Play Minesweeper on a 9x9 board with 10 mines placed randomly
- Reveal cells and flag suspected mines using text commands
- Flood fill reveal for empty cells adjacent to no mines
- Save and load game progress to / from a file
- Win by clearing all non - mine cells
- Lose by revealing a mine

## Directory Structure
- main.py  : Entry point to run the game in CLI mode
- board.py : Contains the Board and Cell classes, mine placement, calculating adjacency, cell operations
- game_logic.py: Win and loss checking operations
- file_manager.py: Save and load game state

## Game Instructions
- Run the game by entering 'python main.py' in the terminal
- Enter 1 for new game or 2 for loading the previously saved game
- Use the following commands:
- 'r row col' to reveal a cell. Ex: If u want to reveal (1,2) enter r 1 2
- 'f row col' to flag a cell. Ex: If u want to flag (1,2) enter f 1 2
- 's' to save the current game progress
- 'q' to quit the game
- Game objective: Reveal all non-mine cells without landing on a mine to win

## Setup Instructions
- Ensure Python 3 is installed
- Place all project files in the directory
- Run the game using 'python main.py' in the terminal
- Use the commands listed to interact with the game
- Game save files are stored at 'data/minesweepersave.txt'

## Team Members
- Aditya Unnithan : board.py
- Aryan Mahendra Sawant : README.md and assisted in board.py
- Bayyapu Adhiraj Reddy : main.py
- Bhargav Kumar Gudipati : game_logic.py and assisted in main.py
- Kumar Sanket : file_manager.py
