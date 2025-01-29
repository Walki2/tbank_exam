import bisect

def solution(n, s, a):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    result = n * (n + 1) // 2

    for i in range(1, n):
        A = prefix[i] - s
        B = prefix[i + 1] - s

        left = bisect.bisect_left(prefix, A, 0, i)
        right = bisect.bisect_left(prefix, B, 0, i)

        count = right - left
        result += count * (n - i)

    print(result)

n, s = map(int, input().split())
a = list(map(int, input().split()))
