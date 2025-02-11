def totalCost(mask, curr, n, cost, memo, path_tracker):
    if mask == (1 << n) - 1:        # if all cities are visited, return the cost to return to the starting city (0)
        return cost[curr][0]
    
    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')
    best_next_city = -1
    for i in range(n):      # visiting every city that has not been visited yet
        if (mask & (1 << i)) == 0: 
          
          # If city i is not visited
          # Visit city i and update the mask
            result = cost[curr][i] + totalCost(mask | (1 << i), i, n, cost, memo, path_tracker)
            if result < ans:
                ans = result
                best_next_city = i

    # Memoize the result
    memo[curr][mask] = ans
    # Track the best path
    path_tracker[curr][mask] = best_next_city
    return ans


def reconstructPath(n, cost, memo, path_tracker):
    mask = 1  # start with city 0 visited
    curr = 0
    path = [curr]
    while True:
        next_city = path_tracker[curr][mask]
        if next_city == -1:
            break
        path.append(next_city)
        mask |= (1 << next_city)
        curr = next_city
    return path


def tsp(cost):
    n = len(cost)
    
    # Initialize memoization table with -1
    # (indicating uncomputed states)
    memo = [[-1] * (1 << n) for _ in range(n)]
    # Initialize path tracker to store the best path at each step
    path_tracker = [[-1] * (1 << n) for _ in range(n)]
    
    # Start from city 0, with only city 0 visited initially (mask = 1)
    total_cost = totalCost(1, 0, n, cost, memo, path_tracker)
    # Reconstruct the optimal path
    path = reconstructPath(n, cost, memo, path_tracker)
    return total_cost, path


# Example cost matrix
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Call tsp function to get the minimum cost and the optimal path
total_cost, path = tsp(cost)

print(f"Minimum Cost: {total_cost}")
print(f"Optimal Path: {path}")
