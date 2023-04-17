# height = index+1
# 가장 작은것부터 시작해, 자기 오른쪽에 자기보드 키가 큰 사람의 수 만큼 index swap(?)


n = int(input())
l = list(map(int,input().split()))
result = [0]*n

for a in range(n):
    tmp_a = a+1
    
    while result[l[a]] != 0 and l[a] < n-1:
        l[a] += 1    
    result[l[a]] = tmp_a

print(*result)
