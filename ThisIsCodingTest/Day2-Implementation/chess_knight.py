x,y = input().split()

alpha = ['a','b','c','d','e','f','g','h']
num = [1,2,3,4,5,6,7,8]
count = 0

index_alpha = alpha.index(x) +1
index_num = num.index(int(y)) + 1

if (index_alpha-2) > 0 and (index_num - 3) > 0:
  count += 1
if (index_alpha-2) > 0 and (index_num + 3) > 0:
  count += 1
if (index_alpha-3) > 0 and (index_num - 2) > 0:
  count += 1
if (index_alpha-3) > 0 and (index_num + 2) > 0:
  count += 1
if (index_alpha+2) > 0 and (index_num - 3) > 0:
  count += 1
if (index_alpha+2) > 0 and (index_num + 3) > 0:
  count += 1
if (index_alpha+3) > 0 and (index_num - 2) > 0:
  count += 1
if (index_alpha+3) > 0 and (index_num + 2) > 0:
  count += 1

print(count)