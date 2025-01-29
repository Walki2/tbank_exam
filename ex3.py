def min_adjustments(n, m, a):
    a1 = a[0]
    a2 = a[1]

    lower_bound = min(a1, a2)
    upper_bound = max(a1, a2)

    adjustments = []

    for i in range(2, n):
        if a[i] < lower_bound:
            adjustments.append(lower_bound - a[i])
        elif a[i] > upper_bound:
            adjustments.append(a[i] - upper_bound)

    adjustments.sort()

    return sum(adjustments[:m])



n, m = map(int, input().split())
a = list(map(int, input().split()))

print(min_adjustments(n, m, a))
