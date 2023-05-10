t = int(input())

results = []
for _ in range(t):
    team = []

    for _ in range(11):
        team.append(list(map(int, input().split())))

    current = []
    filled_position = [False for _ in range(11)]
    current_max = 0

    def combinations(start):
        global current_max
        
        if start == 11:
            current_max = max(current_max, sum(current))
            return
        
        for a in range(start, 11):
            for b in range(11):
                if team[b][a] != 0 and filled_position[b] == False:
                    current.append(team[b][a])
                    filled_position[b] = True
                    combinations(start+1)
                    current.pop()
                    filled_position[b] = False
            return
                    
    combinations(0)
    results.append(current_max)    
    

for a in results:
    print(a)