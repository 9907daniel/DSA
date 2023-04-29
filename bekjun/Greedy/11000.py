n = int(input())

timeslot = []

for _ in range(n):
    timeslot.append(list(map(int, input().split())))
    

tmp = [[]]
current = []

for a in range(len(timeslot)):
    # print(timeslot, tmp)
    for b in range(len(tmp)):
        if timeslot[a][0] not in tmp[b] and timeslot[a][1] not in tmp[b]:
            for c in range(timeslot[a][0], timeslot[a][1]):
                tmp[b].append(c)
            break
        else:
            tmp.append([])
            for c in range(timeslot[a][0], timeslot[a][1]):
                tmp[b+1].append(c)
            break
        
count = 0
for a in range(len(tmp)):
    if len(tmp[a]) != 0:
        count += 1
print(count)
                
