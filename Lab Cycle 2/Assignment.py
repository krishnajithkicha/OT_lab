import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    total_cost = cost_matrix[row_ind, col_ind].sum()
    

    assignment = list(zip(row_ind, col_ind))
    
    return assignment, total_cost


cost_matrix = np.array([
    [9, 11, 14, 11, 7],
    [6, 15, 13, 13, 10],
    [12, 13, 6, 8, 8],
    [11, 9, 10, 12, 9],
    [7, 12, 14, 10, 14]
])

assignment, total_cost = hungarian_algorithm(cost_matrix)

print("Optimal Assignment (Task -> Worker):")
for task, worker in assignment:
    print(f"Task {task} -> Worker {worker}")

print(f"\nTotal Cost of Assignment: {total_cost}")