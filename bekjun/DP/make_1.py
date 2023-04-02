n = int(input())
d = [0] * (n+1)

for i in range(2, n+1) :
    d[i] = d[i-1]+1
    
    if i % 2 == 0:
        d[i] = min(d[i//2]+1, d[i])
    if i % 3 == 0:
        d[i] = min(d[i//3]+1, d[i])
    if i % 5 == 0:
        d[i] = min(d[i//5]+1, d[i])

print(d[n])




# def make_one(a, count):
#     if a != 1:
#         if a % 5 == 0:
#             make_one(a/5, count+1)
#         elif a % 3 == 0:
#             make_one(a/3, count+1)
#         elif a % 2 == 0:
#             make_one(a/2, count+1)
#         else:
#             make_one(a-1,count+1)
#     else:
#         return count

# print(make_one(26,0))