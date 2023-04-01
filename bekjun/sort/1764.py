n, m = map(int, input().split())

n_list = []
m_list = []

for a in range(n):
    n_list.append(input())

for a in range(m):
    m_list.append(input())

count = 0
tmp = []

result = sorted(m_list&n_list)


# n_list.sort()
# m_list.sort()

# for a in range(len(n_list)):
# for a in m_list:
#     if a in n_list:
#         count += 1
#         tmp.append(a)

# print(count)
# for a in tmp:
#     print(a)
