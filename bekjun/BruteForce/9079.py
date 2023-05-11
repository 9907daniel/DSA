t = int(input())

results = []
for _ in range(t):
    board = []
    for _ in range(3):
        board.append(list(map(int, input().split())))   
  
    visited = [[False]*3 for _ in range(3)]
  
    def combination(board):
        count = 0
        current_count = 999
        if 'H' not in board:
            current_count = min(count, current_count)
            return 
        elif 'T' not in board:
            current_count = min(count, current_count)
            return
        else:
            for a in range(3):
                for b in range(3):
                    
                    tmp_board = board[:]
                    
                    for c in range(3):
                        if board[a][c] == 'H':
                            board[a][c] == 'T'
                        elif board[a][c] == 'T':
                            board[a][c] == 'H'
                    combination(board)
                    board = tmp_board
                        board[a][c] = 
                    
                    board[a][b] =
                    
            
            
    