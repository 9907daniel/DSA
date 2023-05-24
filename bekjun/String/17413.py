s = [a for a in input()]

current = True
tmp = []
result = []

for a in range(len(s)):
    if s[a] == "<":
        tmp.append(s[a])
        current = False
    elif s[a] == ">":
        tmp.append(s[a])
        current = True
        for a in range(len(tmp)):
            result.append(tmp[a])
    elif current == False:
        tmp.append(s[a])
    
    if s[a] != " " and current:
        tmp.append(s[a])
    
    elif s[a] == " " and current or a == len(s)-1 and current:
        reversed = [tmp[a] for a in range(len(tmp)-1,-1,-1)]
        for a in range(len(reversed)):
            result.append(reversed[a])
        tmp = []
            
print(*result)

