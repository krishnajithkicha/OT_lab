import numpy as np

def vogel_approximation_method(supply, demand, costs):
    # Convert costs to float to handle np.inf assignments
    costs = costs.astype(float)
    transportation_plan = np.zeros_like(costs)
    total_cost = 0

    # Keep track of remaining supply and demand
    remaining_supply = supply.copy()
    remaining_demand = demand.copy()

    while np.sum(remaining_supply) > 0 and np.sum(remaining_demand) > 0:
        # Calculate row and column penalties
        row_penalties = []
        col_penalties = []

        # Calculate row penalties
        for i in range(costs.shape[0]):
            if remaining_supply[i] > 0:
                row_cost = costs[i, :]
                valid_cost = sorted([cost for cost in row_cost if cost != np.inf])
                if len(valid_cost) > 1:
                    row_penalties.append(valid_cost[1] - valid_cost[0])
                else:
                    row_penalties.append(0)
            else:
                row_penalties.append(-1)  # Mark as exhausted

        # Calculate column penalties
        for j in range(costs.shape[1]):
            if remaining_demand[j] > 0:
                col_cost = costs[:, j]
                valid_cost = sorted([cost for cost in col_cost if cost != np.inf])
                if len(valid_cost) > 1:
                    col_penalties.append(valid_cost[1] - valid_cost[0])
                else:
                    col_penalties.append(0)
            else:
                col_penalties.append(-1)  # Mark as exhausted

        # Determine whether to consider row or column penalty
        max_row_penalty = max([penalty for penalty in row_penalties if penalty >= 0], default=-1)
        max_col_penalty = max([penalty for penalty in col_penalties if penalty >= 0], default=-1)

        if max_row_penalty >= max_col_penalty:
            row_idx = row_penalties.index(max_row_penalty)
            col_idx = np.argmin(costs[row_idx, :])  # Choose the lowest cost in the row
        else:
            col_idx = col_penalties.index(max_col_penalty)
            row_idx = np.argmin(costs[:, col_idx])  # Choose the lowest cost in the column

        # Allocate the supply and demand
        allocated = min(remaining_supply[row_idx], remaining_demand[col_idx])
        transportation_plan[row_idx, col_idx] = allocated
        total_cost += allocated * costs[row_idx, col_idx]

        # Update supply and demand
        remaining_supply[row_idx] -= allocated
        remaining_demand[col_idx] -= allocated

        # Mark exhausted rows and columns as np.inf
        if remaining_supply[row_idx] == 0:
            costs[row_idx, :] = np.inf
        if remaining_demand[col_idx] == 0:
            costs[:, col_idx] = np.inf

    return transportation_plan, total_cost

# Example usage
supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])
costs = np.array([
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8, 3, 3, 2]
])

plan, cost = vogel_approximation_method(supply, demand, costs)
print("Optimal Transportation Plan:")
print(plan)
print("Total Transportation Cost:", cost)