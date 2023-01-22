n, m, k = map(int, input().split())
list_a = list(map(int, input().split()))

list_a.sort()
count = 0
count_consecutive = 0
total = 0

print(list_a)

while count < m:
  if count_consecutive < k:
    total = total + list_a[-1]
    count += 1
  else:
    total = total + list_a[-2]
    count += 1

print(total)

