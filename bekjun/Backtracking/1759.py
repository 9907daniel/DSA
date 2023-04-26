l, c = map(int, input().split())

letters = list(map(str, input().split()))
letters.sort()

potential = []
tmp = []
vowls = ['a','e','i','o','u']
vowl_count = 0
non_vowl_count = 0
visited = [False for _ in range(len(letters))]

def combinations(start):
    global vowl_count
    global non_vowl_count

    
    if start == l and vowl_count > 0 and non_vowl_count > 1:
        tmp.sort()
        if tmp not in potential:
            potential.append(tmp[:])
        return
    
    for a in range(start, len(letters)):
        if visited[a] == False and letters[a] not in tmp:
            
            visited[a] = True
            tmp.append(letters[a])

            if letters[a] not in vowls:
                non_vowl_count += 1
            else:
                vowl_count += 1
                
            combinations(start + 1)
            
            tmp.pop()
            visited[a] = False
            if letters[a] not in vowls:
                non_vowl_count -= 1
            else:
                vowl_count -= 1
            
combinations(0)
print(potential)

