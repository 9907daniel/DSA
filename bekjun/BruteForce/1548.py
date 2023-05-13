# https://www.acmicpc.net/submit/1548
# Gold 5 Brute Force

# 풀이 2)
# 정렬을 이용해 sliding window 와 같은 for, while loop을 활용함
# 기본적으로 2 이상이면 적어도 최소 수열은 2는 가능하다


# 예시 ) l = [1,2,3,4,5,6,7]
# 3 이상부터는 3부터 시작해서 1,2,3 -> 2,3,4 -> 3,4,5 ...
# 4 는 4부터 1,2,3,4 -> 2,3,4,5
# 여기서 중요한거는 조합을 비교할때, l[-1] < l[0] + l[1] 만 비교하면된다

from itertools import combinations

n = int(input())
l = list(map(int, input().split()))
sorted_l = sorted(l)


if n == 1:
    count = 1
elif n > 1:
    count = 2

for a in range(3, len(sorted_l)+1):
    start = 0
    current = a
    while current < len(sorted_l)+1:
        tmp = []
        tmp = sorted_l[start:current]
        if tmp[-1] < tmp[0] + tmp[1]:
            count = a
            break
        start += 1
        current += 1

print(count)


# 풀이 1) 시간초과 ..

# 최대 삼각 수열 list 를 찾기 위한 문제
# 1. 우선 주어진 배열 for loop을 통해 1개 길이 부터 시작 해서 하나씩 더 증가시킨다
# 2. 만약 길이가 더 긴 배열의 조합이 삼각수열이 가능하다면 (function이 True를 반환헸디먄)max(current, new)를 통해 +1을 한다


# def check(potential):
#     answer = True                   # True로 시작
#     c = combinations(potential, 3)  # 지금 list의 모든 3개 조합을 만들어보기
#     for d in c:                     # 조합 모두 확인
#         if d[0] >= d[1]+d[2] or d[1] >= d[2]+d[0] or d[2] >= d[1]+d[0]:
#             answer = False
#     if answer:
#         return len(potential)
#     return 0

# count = 0
# for a in range(1,len(l)+1):         # 1~len(l) 까지 최대 길이로 combination 측정
#     types = combinations(l,a)       # n 짜리의 모든 조합.. 
#     for b in types:                 # 모든 조합 중 하나라도 가능한것이 있는지..
#         checkout = check(b)         # check function에 list 보내기
#         count = max(count, checkout)
                
# print(count)
