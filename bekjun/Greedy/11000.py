import heapq

n = int(input())

timeslot = []

for _ in range(n):
    timeslot.append(list(map(int, input().split())))
    
timeslot.sort(key = lambda x: x[0])

h = [timeslot[0][1]]
heapq.heapify(h)

for a in range(1, len(timeslot)):
    if timeslot[a][0] >= h[0]:
        # h[0] will always be the smallest
        heapq.heappop(h)
        heapq.heappush(h, timeslot[a][1])
    else:
        heapq.heappush(h, timeslot[a][1])

print(h)





# current = [timeslot[0][1]]
# for a in range(1, len(timeslot)):
#     if timeslot[a][0] >= current:
#         current = timeslot[a][1]
        
#     elif 
    # if current start time is equalr to or greater than meeting room
    # we make it the end time
    # else, we make a new room
    
    
    
    
    
    
    
    
    
    

# rooms = [timeslot[0][1]]
# for a in range(1, len(timeslot)):
    
#     for b in range(len(rooms)):
#         if timeslot[a][0] >= rooms[b]:
#             rooms[b] = timeslot[a][1]
#             break
#         elif b == len(rooms)-1 and timeslot[a][0] < rooms[b]:
#             rooms.append(timeslot[a][1])
    
# print(len(rooms))



# count = 0

# current_max = timeslot[0][0]
# for a in range(1, len(timeslot)):
#     if current_max >= timeslot[a][1]:
#         current_max = timeslot[a][0]
#     else:
#         count += 1
#         current_max = timeslot[a][0]

# print(count)




# result = [timeslot[0][1]]

# for a in range(len(timeslot)):
#     if timeslot[a][0] >= result[a]
        
    
    
    
    
    

