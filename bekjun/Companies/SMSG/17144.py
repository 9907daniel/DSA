r,c,t = map(int, input().split())
l = []
for a in range (r):
    l.append(list(map(int, input().split())))
    
spread = [1,-1,1,-1]
sucker = []
    
def spread(l):
    # for a in range(t):
    directions = 0
    for i in range(r):
        for j in range(c):
            if l[i][j] != 0 and l[i][j] != -1:
                spreaded = int(l[i][j]//5)
                if i-1 >= 0:
                    if l[i-1][j] != -1:
                        l[i-1][j] += spreaded
                        directions += 1
                if i+1 < r:
                    if l[i+1][j] != -1:
                        l[i-1][j] += spreaded
                        directions += 1
                if j-1 >= 0:
                    if l[i][j-1] != -1:
                        l[i][j-1] += spreaded
                        directions += 1                        
                if j+1 < c:
                    if l[i][j+1] != -1:
                        l[i][j+1] += spreaded
                        directions += 1                        
                l[i][j] = l[i][j] -(spreaded)*directions
    return l

# print(spread(l))

def clear_up(l):
    for i in range(r):
        for j in range(c):
            if 0<=i<=1 and j == 0:
                if l[i+1][j] == -1:
                    l[i][j] = l[i-1][j]
                else: 
                    l[i][j] = l[i][j+1]
            elif i == 1:
                for k in range(7):
                    l[i][k] = l[i][k+1]
                if j == 7:
                    l[i][j] = l[i][j+1]
            elif j == 7 and 1 <= i < 2:
                l[i][j] = l[i+1][j]
            elif i == 2:
                for k in range(2, 7):
                    l[i][k] = l[i][j-1]
                if j == 1:
                    l[i][j] = 0
                    
    for i in range(r):
        for j in range(c):
            if j == 3:
                if i != 1:
                    l[i][j] = 0
                else:
                    l[i][j] = l[i][j-1]
                
                
                
                if l[i-1][j] == -1:
                    l[i][j] = l[i-1][j]
                else: 
                    l[i][j] = l[i][j+1]
            elif i == 1:
                for k in range(7):
                    l[i][k] = l[i][k+1]
                if j == 7:
                    l[i][j] = l[i][j+1]
            elif j == 7 and 1 <= i < 2:
                l[i][j] = l[i+1][j]
            elif i == 2:
                for k in range(2, 7):
                    l[i][k] = l[i][j-1]
                if j == 1:
                    l[i][j] = 0
                


def solution(new_l):
    for a in range(t):
        new_l = spread(new_l)
        clear(new_l)
            
solution(l)
    