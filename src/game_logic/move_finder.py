# src/game_logic/move_finder.py

class MoveFinder:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def find_moves(self, grid):
        moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                # Check horizontal swap
                if j < self.cols - 1:
                    if self._check_move(grid, i, j, i, j+1):
                        moves.append(((i, j), (i, j+1)))
                # Check vertical swap
                if i < self.rows - 1:
                    if self._check_move(grid, i, j, i+1, j):
                        moves.append(((i, j), (i+1, j)))
        return moves

    def _check_move(self, grid, r1, c1, r2, c2):
        # Swap gems
        grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
        
        valid = self._check_matches(grid, r1, c1) or self._check_matches(grid, r2, c2)
        
        # Swap back
        grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
        
        return valid

    def _check_matches(self, grid, r, c):
        # Check for horizontal matches
        if c > 1 and grid[r][c] == grid[r][c-1] == grid[r][c-2]:
            return True
        if c < self.cols - 2 and grid[r][c] == grid[r][c+1] == grid[r][c+2]:
            return True
        
        # Check for vertical matches
        if r > 1 and grid[r][c] == grid[r-1][c] == grid[r-2][c]:
            return True
        if r < self.rows - 2 and grid[r][c] == grid[r+1][c] == grid[r+2][c]:
            return True
        
        return False