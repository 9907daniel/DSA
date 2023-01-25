input_data = input()
column = (int(ord(input_data[0])) - int(ord("a"))) +1
row = int(input_data[1])

moveset = [[-2,-1],[-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,2],[1,-2]]
count = 0

for move in moveset:
  next_column = column - move[0]
  next_row = row - move[1]

  if next_column >= 1 and next_row >=1 and next_column <= 8 and next_row <=8:
    count += 1

print(count)
  