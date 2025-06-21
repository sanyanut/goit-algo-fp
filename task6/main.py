def greedy_algorithm(items, budget):
    item_ratios = {}
    for item, data in items.items():
        if data["cost"] > 0:
            item_ratios[item] = data["calories"] / data["cost"]
        else:
            item_ratios[item] = float("inf")

    sorted_items = sorted(item_ratios.items(), key=lambda x: x[1], reverse=True)

    chosen_items = []
    total_calories = 0
    remaining_budget = budget

    for item_name, _ in sorted_items:
        item_data = items[item_name]
        cost = item_data["cost"]
        calories = item_data["calories"]

        if remaining_budget >= cost:
            chosen_items.append(item_name)
            total_calories += calories
            remaining_budget -= cost

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    item_list = [(name, data["cost"], data["calories"]) for name, data in items.items()]
    n = len(item_list)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, cost, calories = item_list[i - 1]
        for j in range(1, budget + 1):
            if cost <= j:
                dp[i][j] = max(calories + dp[i - 1][j - cost], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    chosen_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        item_name, cost, calories = item_list[i - 1]
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(item_name)
            j -= cost
        i -= 1

    chosen_items.reverse()

    return chosen_items, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

print(f"Available budget: {budget}\n")

greedy_chosen_items, greedy_total_calories = greedy_algorithm(items, budget)
print(f"Greedy algorithm:")
print(f"Selected dishes: {greedy_chosen_items}")
print(f"Total calories: {greedy_total_calories}\n")

dp_chosen_items, dp_total_calories = dynamic_programming(items, budget)
print(f"Dynamic programming:")
print(f"Selected dishes: {dp_chosen_items}")
print(f"Total calories: {dp_total_calories}\n")
