import numpy as np

def simplex(c, A, b):

    num_vars = len(c)
    num_constraints = len(b)

    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))

    for i in range(num_constraints):
        tableau[i, :num_vars] = A[i]
        tableau[i, num_vars + i] = 1  
        tableau[i, -1] = b[i]

    tableau[-1, :num_vars] = -c

    while np.any(tableau[-1, :-1] < 0): 

        pivot_col = np.argmin(tableau[-1, :-1])

        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios < 0] = np.inf  
        pivot_row = np.argmin(ratios)

        pivot_value = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_value

        for i in range(num_constraints + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    optimal_solution = tableau[:-1, -1]
    max_value = tableau[-1, -1]

    return optimal_solution, max_value

c = np.array([2, 3, 1])

A = np.array([
    [1, 1, 1],
    [1, 2, -1]
])

b = np.array([4, 2])

optimal_solution, max_value = simplex(c, A, b)

print("Optimal solution (u1, u2, u3):", optimal_solution)
print("Maximum profit:", max_value)