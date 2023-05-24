# 릿코드 문제 Palindrom에 추가 조건을 추가한 문제이다
# 사실 이 조건이 조금 더 복잡? 하게 만들었다
# pop()하면서 큐나 스택을 사용하는 방법을 처음 시도해 봤으나, 조건 때문에 힘들어 보였다
# 두번째 풀이로는 투 포인터를 사용하면서 비교하는거를 생각했다

n = int(input())
l = []
for _ in range(n):
    l.append(list([a for a in input()]))    
results = []

for a in l:
    start = 0
    end = len(a)-1
    count = 0
    while start < end:
        if a[start] != a[end]:
            count += 1
            if a[start+1] ==[end]:
                if a[start+2] == a[end-1]:
                    start += 1
            if a[end-1] == a[start]:
                if a[end-2] == a[start+1]:
                    end -= 1
            else:
                count += 1
                break
        start += 1
        end -= 1
        
    if count < 2:
        results.append(count)
    else:
        results.append(2)

for a in results:
    print(a)
    
        
    