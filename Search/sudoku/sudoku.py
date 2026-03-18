from csp import CSP

puzzle = [[0, 0, 9, 5, 8, 6, 0, 0, 0],
          [0, 0, 0, 0, 2, 0, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 6, 8, 3],
          [9, 0, 0, 6, 5, 0, 0, 3, 2],
          [0, 6, 0, 7, 0, 0, 0, 9, 8],
          [0, 3, 0, 2, 0, 0, 7, 0, 4],
          [0, 0, 3, 0, 0, 0, 0, 0, 0],
          [6, 2, 0, 0, 1, 5, 0, 4, 0],
          [0, 0, 0, 4, 0, 0, 0, 5, 0]]

def print_sudoku(puzzle):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(puzzle[i][j], end=" ")
        print()

variables = [(i, j) for i in range(9) for j in range(9)]

domains = {
    var: set(range(1, 10)) if puzzle[var[0]][var[1]] == 0 else {puzzle[var[0]][var[1]]}
    for var in variables
}

constraints = {}

def add_constraint(var):
    constraints[var] = []
    for i in range(9):
        if i != var[0]:
            constraints[var].append((i, var[1]))  
        if i != var[1]:
            constraints[var].append((var[0], i))  
    sub_i, sub_j = var[0] // 3, var[1] // 3
    for i in range(sub_i * 3, (sub_i + 1) * 3):
        for j in range(sub_j * 3, (sub_j + 1) * 3):
            if (i, j) != var:
                constraints[var].append((i, j))  

for var in variables:
    add_constraint(var)

csp = CSP(variables, domains, constraints)
sol = csp.solve()

solution = [[0 for _ in range(9)] for _ in range(9)]
for (i, j), val in sol.items():
    solution[i][j] = val

print("\n******* Solution *******\n")
print_sudoku(solution)
print(csp.backtracks)