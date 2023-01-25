n = int(input())
count = 0
x, y = 1, 1

cmd = list(input("input L R U D : ").split())

nx = [0,0,-1,1]
ny = [-1,1,0,0]
alpha = ["L","R","U","D"]

for a in cmd:
  for b in range(len(alpha)):
      if alpha[b] == a:
        ix = x + nx[b]
        iy = y + ny[b]
  if ix < 1 or iy < 1 or iy >n or iy > n:
    continue

  x = ix
  y = iy
        
print(x, y)

      
  
