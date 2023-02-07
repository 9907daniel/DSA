import heapq

minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)

print(minHeap)
# [2,3,4]
# Min is always at index 0
# minHeap[0] = 2

while len(minHeap):
    print(heapq.heappop(minHeap))
# 2
# 3
# 4
# smallest to largest because min is pop'd


