x, y = map(int, input().split())
dic_a = []
count = 0
empty_list = []

while count < x:
  new_list = list(map(int, input().split()))
  dic_a.append(new_list)
  count += 1
dic_a.sort()

print(dic_a)

for a in dic_a:
  a.sort()
  empty_list.append(a[0])

empty_list.sort()
print(empty_list)
print(empty_list[-1])

# Time 13minutes
# Time complexity : On
# Too much Brute Force
# --> Use min, max