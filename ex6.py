def is_non_degenerate(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) != 0


def max_happy_triplets(n, points):
    happy_triplets = []

    # Генерируем все возможные тройки
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_non_degenerate(points[i], points[j], points[k]):
                    happy_triplets.append((i, j, k))

    used = [False] * n
    count = 0

    for triplet in happy_triplets:
        if not used[triplet[0]] and not used[triplet[1]] and not used[triplet[2]]:
            used[triplet[0]] = True
            used[triplet[1]] = True
            used[triplet[2]] = True
            count += 1

    return count


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

print(max_happy_triplets(n, points))
