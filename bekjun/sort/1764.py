# https://www.acmicpc.net/problem/1764
# 듣도 보도 못한 사람 수 찾기

n, m = map(int, input().split())
n_list = set()
m_list = set()
for _ in range(n):
    n_list.add(input())
for _ in range(m):
    m_list.add(input())


tmp = sorted(list(n_list&m_list))

print(len(tmp))
for a in tmp:
    print(a)

# count = 0
# tmp = []

# for a in n_list:
#     if a in m_list:
#         tmp.append(a)
#         count += 1
        
# print(count)
# tmp.sort()

# for a in range(len(tmp)):
#     print(tmp[a])




