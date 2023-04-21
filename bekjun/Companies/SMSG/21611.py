# 1. 파괴
# 2. 변경
# 3. 옮기기
# 4. 폭발

def destroy(d, s):
    global board, N, shark

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, s + 1):
        nx = shark[0] + dx[d - 1] * i
        ny = shark[1] + dy[d - 1] * i

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            break

        board[nx][ny] = 0


def convert():
    global board

    arr = []
    cur = shark[:]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    num = 1
    direction = 0
    is_over = False
    while not is_over:
        for i in range(2):
            for j in range(num):
                cur[0] += dx[direction]
                cur[1] += dy[direction]

                if cur[0] < 0 or cur[1] < 0 or cur[0] >= N or cur[1] >= N:
                    is_over = True
                    break
                
                arr.append(board[cur[0]][cur[1]])
            direction = (direction + 1) % 4
            if is_over:
                break
        num += 1

    return arr


def move(arr):
    return [arr[i] for i in range(len(arr)) if arr[i] != 0]

def explode(arr):
    global result

    if not arr:
        return [], False

    cur_marble = arr[0]
    cur_num = 1
    is_removed = False

    for i in range(1, len(arr)):
        if arr[i] == cur_marble:
            cur_num += 1
        else:
            if cur_num < 4:
                cur_num = 1
                cur_marble = arr[i]
            else:
                for j in range(1, cur_num + 1):
                    arr[i - j] = 0
                result[cur_marble - 1] += cur_num
                is_removed = True
                cur_num = 1
                cur_marble = arr[i]
    if cur_num >= 4:
        is_removed = True
        for j in range(1, cur_num + 1):
            arr[len(arr) - j] = 0
        result[cur_marble - 1] += cur_num

    return arr, is_removed



N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
blizard = [[] for _ in range(M)]
for i in range(M):
    blizard[i] = list(map(int, input().split()))
shark = [(N - 1) // 2, (N - 1) // 2]
result = [0, 0, 0]



def solution():
    global M, blizard, board, result

    for i in range(M):
        destroy(blizard[i][0], blizard[i][1])  # 방향, 거리
        arr = convert()
        arr = move(arr)


solution()