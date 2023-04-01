n, m = map(int, input().split())
food = list(map(int, input().split()))

## Brute Force --> Most likley Timeout

# def cut_food(food, start, count):
#     while count < m:
#         for a in food:
#             if a - start > 0:
#                 count += (a-start)
#         start -= 1
#     return start


# print(cut_food(food, max(food)-1, 0)



## Binary Search Tree

def binary_cut(start,end,middle,food):
    # while start <= end
    middle = (start + end) //2
    total = 0
    for a in food:
        if a > food[middle]:
            total += (a-food[middle])
    return total
            
        
food.sort()
start = 0
end = len(food)-1
middle = (start+end)//2

while start <= end:
    if binary_cut(start, end, middle, food) > m:
        start = middle +1
    elif binary_cut(start, end, middle, food) < m:
        end = middle - 1
    else:
        print(middle)
        start = end + 1

            