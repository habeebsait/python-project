def knapsack_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


if __name__ == "__main__":

    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7


    max_value = knapsack_optimized(weights, values, capacity)
    

    print(f"The maximum value that can be taken in the knapsack is: {max_value}")
