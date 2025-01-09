# https://www.acmicpc.net/problem/16435

_, start = map(int, input().split())
for i in sorted(map(int, input().split())):
    if start >= i:
        start += 1
print(start)