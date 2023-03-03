a = list(map(int,input().split()))


result_has_to_be = [1,1,2,2,2,8]
res = []


for b in range(len(a)):
    res.append(result_has_to_be[b]-a[b])

print(res)



