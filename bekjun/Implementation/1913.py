n = int(input())
key = int(input())

graph = [[0]*n for _ in range(n)]

start = n//2 

graph[start][start] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn():
    turns = 1
    direction = 0
    start_x = n//2
    start_y = n//2
    
    current = 1
        
    while True:
        if direction == 4:
            direction = 0
            
        for _ in range(2):
            for _ in range(turns):
                current += 1
                start_x = start_x + dx[direction]     
                start_y = start_y + dy[direction]
                graph[start_x][start_y] = current
                if current == (n*n):
                    return False
            direction += 1
        turns += 1
        
turn()

for a in range(n):        
    print(*graph[a])

for a in range(n):
    for b in range(n):
        if graph[a][b]  == key:
            print(a+1, b+1)       
        

            
# [[49, 26, 27, 28, 29, 30, 31], 
#  [48, 25, 10, 11, 12, 13, 32], 
#  [47, 24, 9, 2, 3, 14, 33], 
#  [46, 23, 8, 1, 4, 15, 34], 
#  [45, 22, 7, 6, 5, 16, 35], 
#  [44, 21, 20, 19, 18, 17, 36], 
#  [50, 42, 41, 40, 39, 38, 37]]