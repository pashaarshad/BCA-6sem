def is_safe(b, row, col, n):
    # Check column
    for i in range(row):
        if b[i][col] == "Q":
            return False

    # Check left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if b[i][j] == "Q":
            return False

    # Check right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if b[i][j] == "Q":
            return False

    return True


def solve_q(b, row, n):
    if row == n:
        for i in range(n):
            print("".join(b[i]))
        print()
        return True  # Found at least one solution

    found = False
    for col in range(n):
        if is_safe(b, row, col, n):
            b[row][col] = "Q"
            found = solve_q(b, row + 1, n) or found
            b[row][col] = "X"

    return found


def start(n):
    b = [["X" for _ in range(n)] for _ in range(n)]

    if not solve_q(b, 0, n):
        print("No Solution")


n = 4
start(n)