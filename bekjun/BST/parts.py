import sys

n = int(input())
l = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))


def binary_search(target, stock, start,end):
    while start <= end:
        middle = (start+end)//2
        if target > stock[middle]:
            start = middle + 1 
        elif target < stock[middle]:
            end = middle - 1
        else:
            return("Yes")
    return("No")
    
    
for i in check:
    print(binary_search(i, l, 0, len(l)-1))
    