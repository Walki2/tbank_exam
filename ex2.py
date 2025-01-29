def find_max_bouquet_cost(budgets):
    flower_costs = [2 ** i for i in range(61)]
    flower_costs.sort()
    results = []

    for budget in budgets:
        max_cost = -1
        length = len(flower_costs)

        for i in range(length):
            j = i + 1
            k = length - 1

            while j < k:
                total_cost = flower_costs[i] + flower_costs[j] + flower_costs[k]
                if total_cost <= budget:
                    max_cost = max(max_cost, total_cost)
                    j += 1
                else:
                    k -= 1

        results.append(max_cost)

    return results


budgets = [int(input()) for _ in range(int(input()))]
results = find_max_bouquet_cost(budgets)

for result in results:
    print(result)
