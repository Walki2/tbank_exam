
def sol(n, k, a):
    mod = 998244353
    S = [0] * (k + 1)
    S[0] = n % mod  # a_i^0 = 1

    pow_current = [1] * n

    for m in range(1, k + 1):
        total = 0
        for i in range(n):
            pow_current[i] = (pow_current[i] * a[i]) % mod
            total = (total + pow_current[i]) % mod
        S[m] = total

    #C(p, m) mod mod
    comb = [[0] * (k + 1) for _ in range(k + 1)]
    comb[0][0] = 1
    for p in range(1, k + 1):
        comb[p][0] = 1
        comb[p][p] = 1
        for m in range(1, p):
            comb[p][m] = (comb[p - 1][m - 1] + comb[p - 1][m]) % mod

    pow2 = [1] * (k + 1)
    for p in range(1, k + 1):
        pow2[p] = (pow2[p - 1] * 2) % mod

    inv_2 = (mod + 1) // 2

    results = []
    for p in range(1, k + 1):
        sum_binom = 0
        for m in range(p + 1):
            c = comb[p][m]
            sm = S[m]
            spm = S[p - m]
            term = c * sm % mod
            term = term * spm % mod
            sum_binom = (sum_binom + term) % mod

        sum_single = pow2[p] * S[p] % mod
        total = (sum_binom - sum_single) % mod
        if total < 0:
            total += mod
        res = total * inv_2 % mod
        results.append(res)

    return results

n, k = map(int, input().split())
a = list(map(int, input().split()))
result = sol(n, k, a)
for res in result:
    print(res)
