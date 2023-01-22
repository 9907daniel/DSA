n, m, k = map(int, input().split())
list_a = list(map(int, input().split()))

list_a.sort()
first = list_a[-1]
second = list_a[-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
