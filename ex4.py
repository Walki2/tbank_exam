def minimal_operations(n, x, y, z, a):
    def calculate_increase(a_i, d):
        remainder = a_i % d
        return 0 if remainder == 0 else d - remainder

    increases = []
    for a_i in a:
        inc_x = calculate_increase(a_i, x)
        inc_y = calculate_increase(a_i, y)
        inc_z = calculate_increase(a_i, z)
        increases.append((inc_x, inc_y, inc_z))

    min_ops = float('inf')
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total = 0
                if i == j == k:
                    total += max(increases[i][0], increases[i][1], increases[i][2])
                elif i == j:
                    total += max(increases[i][0], increases[i][1]) + increases[k][2]
                elif i == k:
                    total += max(increases[i][0], increases[i][2]) + increases[j][1]
                elif j == k:
                    total += max(increases[j][1], increases[j][2]) + increases[i][0]
                else:

                    total += increases[i][0] + increases[j][1] + increases[k][2]
                if total < min_ops:
                    min_ops = total

    return min_ops

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))

print(minimal_operations(n, x, y, z, a))
