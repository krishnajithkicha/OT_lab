def knapsack(weights, values, capacity):
    n = len(weights)  # number of items
    # Create a DP table with (n+1) rows and (capacity+1) columns
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # if the item can be included
                # Max of not including or including the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # The bottom-right cell contains the maximum value we can get
    return dp[n][capacity]

# Example usage
weights = [2, 3, 4, 5]  # Weights of the items
values = [3, 4, 5, 6]   # Values of the items
capacity = 5            # Capacity of the knapsack

max_value = knapsack(weights, values, capacity)
print(f"Maximum value that can be obtained: {max_value}")
