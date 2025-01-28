from scipy.optimize import linprog

# Coefficients of the objective function (profit)
c = [-20, -30]  # Negating to convert maximization to minimization

# Coefficients of the inequality constraints (Ax <= b)
A = [
    [1, 5],  # x + 5y <= 125 (Wood constraint)
    [3, 1],  # 3x + y <= 80 (Metal constraint)
]

# Right-hand side of the constraints
b = [125, 80]

# Bounds for x and y (non-negativity constraint)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the LP problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Output the results
if result.success:
    x_opt = result.x[0]  # Optimal number of chairs
    y_opt = result.x[1]  # Optimal number of tables
    max_profit = -result.fun  # Convert back to the actual profit (negated in the objective)
    
    print(f"Optimal number of chairs: {int(x_opt)}")
    print(f"Optimal number of tables: {int(y_opt)}")
    print(f"Maximum profit: ${max_profit:.2f}")
else:
    print("No solution found.")
