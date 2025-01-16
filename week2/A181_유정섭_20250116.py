# https://www.acmicpc.net/problem/2588

n = int(input())
m = input()

t = [n * int(a) for a in reversed(m)]
print(*[*t, sum(map(lambda x: x[1] * 10 ** x[0], enumerate(t)))], sep="\n")
