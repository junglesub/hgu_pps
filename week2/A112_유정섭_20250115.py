# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())

manyC = []
singleC = []
for _ in range(m):
    a, b = map(int, input().split())
    manyC.append(a)
    singleC.append(b)

manyC[0] = min(min(singleC) * 6, min(manyC))

print(n // 6 * min(manyC) + min(n % 6 * min(singleC), min(manyC)))
