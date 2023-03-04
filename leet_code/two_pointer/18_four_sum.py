

nums = [1,0,-1,0,-2,2]
target = 0

result = []
nums.sort()

l1,l2,r1,r2 = 0,1, len(nums)-2, len(nums)-1

while l1 != r2 -4:
    while l2 < r1:
        print(l1,l2,r1,r2)
        if nums[l1]+nums[l2]+nums[r1]+nums[r2] > target:
            l2 += 1
        elif nums[l1]+nums[l2]+nums[r1]+nums[r2] < target:
            r1 -= 1
        else:
            result.append([nums[l1],nums[l2],nums[r1],nums[r2]])
            l2 += 1
            r1 -= 1
    l1 += 1
    l2 = l1 + 1
    r2 -= 1
    r1 = r2 -1

print(result)