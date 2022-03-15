from numba import njit, prange


@njit(fastmath=True, cache=True)
def f(x):
    d = [y for y in prange(2, (x // 2) + 1) if x % y == 0]
    d = d[::-1]
    if len(d) >= 3 and (d[0] + d[1] + d[2]) % 2022 == 0 and (d[0] + d[1] + d[2]) != x:
        return (d[0] + d[1] + d[2])


for i in range(1_200_000, 1, -1):
    c = i
    s = f(i)
    if s:
        print(c, s)
