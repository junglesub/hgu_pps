# https://www.acmicpc.net/problem/3059


for _ in range(int(input())):
    alpha = list(range(65, 91))
    for c in input():
        if ord(c) in alpha:
            alpha.remove(ord(c))
    print(sum(alpha))
