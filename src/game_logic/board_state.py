# src/game_logic/board_state.py

class BoardState:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def update_grid(self, new_grid):
        if len(new_grid) != self.rows or any(len(row) != self.cols for row in new_grid):
            raise ValueError("New grid dimensions do not match the board state")
        self.grid = new_grid

    def get_gem(self, row, col):
        return self.grid[row][col]

    def set_gem(self, row, col, gem):
        self.grid[row][col] = gem

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def __str__(self):
        return '\n'.join([' '.join([str(gem or '-') for gem in row]) for row in self.grid])