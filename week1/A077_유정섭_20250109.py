# https://www.acmicpc.net/problem/2822

top5 = sorted(enumerate([int(input()) for x in range(8)]), key=lambda x: x[1])[-5:]
print(sum([x[1] for x in top5]))
print(" ".join(sorted([str(x[0] + 1) for x in top5])))