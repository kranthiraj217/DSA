class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if no queen is present in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper diagonal on right side
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_nqueens(self, row):
        if row == self.n:
            temp_solution = []
            for i in range(self.n):
                temp_solution.append("".join('Q' if x == 1 else '.' for x in self.board[i]))
            self.solutions.append(temp_solution)
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1

                # Recursive call to place queens in the remaining rows
                self.solve_nqueens(row + 1)

                # Backtrack if placing a queen at board[row][col] doesn't lead to a solution
                self.board[row][col] = 0

    def solve(self):
        self.solve_nqueens(0)
        return self.solutions


# Example usage:
if __name__ == "__main__":
    n = 4  # Change n to solve for different board sizes
    nqueens = NQueens(n)
    solutions = nqueens.solve()

    print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
    for solution in solutions:
        for row in solution:
            print(row)
        print()

