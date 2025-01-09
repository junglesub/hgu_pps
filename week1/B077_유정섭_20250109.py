n = int(input())

if n in range(1, 3):
  print(1)
else:
  before1 = 1
  before2 = 1
  for i in range(2, n):
    temp = before2
    before2 = before1
    before1 = before1 + temp
  print(before1)