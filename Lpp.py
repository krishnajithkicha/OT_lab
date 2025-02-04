from scipy.optimize import linprog

# Coefficients of the objective function (maximize p = 2u1 + 3u2 + u3)
# We use negative because linprog minimizes by default
c = [-2, -3, -1]  # Coefficients of the objective function

# Coefficients for the inequality constraints
A = [
    [1, 1, 1],  # u1 + u2 + u3 <= 4
    [-1, -2, 1], # -u1 - 2u2 + u3 <= -2  (rearranged u1 + 2u2 - u3 >= 2)
]

# Right-hand side of the inequality constraints
b = [4, -2]  # Corresponding RHS of the constraints

# Bounds for u1, u2, u3 (all variables are non-negative)
x_bounds = (0, None)  # u1 >= 0
y_bounds = (0, None)  # u2 >= 0
z_bounds = (0, None)  # u3 >= 0

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs')

# Check if the optimization was successful
if result.success:
    # Output the optimal values for u1, u2, u3
    print(f"Optimal u1: {result.x[0]}")
    print(f"Optimal u2: {result.x[1]}")
    print(f"Optimal u3: {result.x[2]}")
    print(f"Maximum p: {-result.fun}")  # We multiply by -1 because we minimized the negative objective function
else:
    print("Optimization failed. Please check the constraints or try again.")