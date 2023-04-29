n,m = map(int, input().split())

max_hour = n*24

initial_score = list(map(int, input().split()))

increase_per_hour = list(map(int, input().split()))

matched = []

for a in range(len(initial_score)):
    matched.append([initial_score[a], increase_per_hour[a]])
    
matched.sort(key=lambda x : x[1], reverse= True)

count = 0
a = 0
while count <= max_hour and a < len(matched):
    if matched[a][0] + matched[a][1] < 100:
        matched[a][0] += matched[a][1]
    elif matched[a][0] + matched[a][1] >= 100:
        matched[a][0] = 100
        a += 1
    else:
        a += 1
    count += 1

total = 0
for a in range(len(matched)):
    total += matched[a][0]

print(total)