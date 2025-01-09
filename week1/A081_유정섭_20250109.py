# https://www.acmicpc.net/problem/2693

for i in range(int(input())):
    print(sorted(map(int, input().split()))[-3])