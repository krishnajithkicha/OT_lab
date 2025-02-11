from scipy.optimize import linprog

# Coefficients of the objective function (profit)
c = [-200, -150]  # Negating to convert maximization to minimization

# Coefficients of the inequality constraints (Ax <= b)
A = [
    [1, 1],         # x + y <= 60 (Total land constraint)
    [20, 10],       # 20x + 10y <= 1200 (Fertilizer constraint)
    [10, 15],       # 10x + 15y <= 600 (Insecticide constraint)
]

# Right-hand side of the constraints
b = [60, 1200, 600]

# Bounds for x and y (Non-negativity and minimum acres constraints)
x_bounds = (20, None)  # At least 20 acres of wheat
y_bounds = (10, None)  # At least 10 acres of barley

# Solve the LP problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Output the results
if result.success:
    x_opt = result.x[0]  # Optimal number of acres of wheat
    y_opt = result.x[1]  # Optimal number of acres of barley
    max_profit = -result.fun  # Convert back to the actual profit (negated in the objective)
    
    print(f"Optimal number of acres of wheat: {x_opt:.2f}")
    print(f"Optimal number of acres of barley: {y_opt:.2f}")
    print(f"Maximum profit: ${max_profit:.2f}")
else:
    print("No solution found.")
