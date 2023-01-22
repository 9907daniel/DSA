x, y = map(int, input().split())
result = 0

for i in range(x):
  list_a = map(int, input().split())
  data = min(list_a)
  result = max(result, data)

print(result)