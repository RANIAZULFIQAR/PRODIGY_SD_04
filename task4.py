class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def print_grid(self):
        for row in self.grid:
            for num in row:
                print(num, end=" ")
            print()  # Move to the next line after printing all numbers in the row

    def is_valid(self, row, col, num):
        # Check if the number is not in the current row, column, and 3x3 sub-grid
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self):
        # Find the next empty cell
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0  # Backtrack
                    return False
        return True


def input_sudoku():
    print("Enter the Sudoku puzzle (9 rows, 9 numbers in each row, use 0 for empty spaces):")
    grid = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
                if len(row) != 9 or not all(0 <= num <= 9 for num in row):
                    raise ValueError
                grid.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter 9 numbers separated by spaces, using 0 for empty cells.")
    return grid


def main():
    grid = input_sudoku()
    solver = SudokuSolver(grid)
    print("\nUnsolved Sudoku grid:")
    solver.print_grid()

    if solver.solve():
        print("\nSudoku puzzle solved:")
        solver.print_grid()
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
