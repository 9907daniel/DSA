n = int(input())

count = 0

n = n % 5
count = n //5

print(n)
while n >= 0:
    n = n - 2
    count += 1

print(count)