from itertools import permutations


calculate = ['+','-','*', '/']
calculated = []
l = list(map(int, input().split()))

for i in range(len(calculate)):
    for b in range(l[i]):
        calculated.append(calculate[i])
        
combinations = list(permutations(calculated, len(calculated)))

print(combinations)

