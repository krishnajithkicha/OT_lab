from scipy.optimize import linprog

# Coefficients of the objective function (maximize revenue)
c = [-5, -3]  # negative because linprog minimizes by default

# Coefficients of the inequality constraints (LHS)
A = [
    [2, 1],  # 2x + y <= 500
    [1, 1]   # x + y <= 400
]

# RHS of the inequality constraints
b = [500, 400]

# Coefficients of the lower bounds (demand constraints)
x_bounds = (100, None)  # x >= 100
y_bounds = (50, None)   # y >= 50

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Output the result
print("Optimal number of chocolate cakes (x):", result.x[0])
print("Optimal number of vanilla cakes (y):", result.x[1])
print("Maximum revenue:", -result.fun)
