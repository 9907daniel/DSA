n = input()
l = [int(a) for a in n]

a = 1
while a != (len(l)) and len(l) > 1:
    if l[a] == l[a-1]:
        l.pop(a)        
    else:
        a += 1

# print(l)

count = 0
for a in l:
    if a == 0:
        count += 1

flip = 0
if count >= (len(l)-count):
    tmp = 0
    for a in range(len(l)):
        if l[a] != tmp and l[a] == 1:
            flip += 1
            tmp = 1
        elif l[a] != tmp and l[a] == 0:
            tmp = 0
else:
    tmp = 1
    for a in range(len(l)):
        if l[a] != tmp and l[a] == 0:
            flip += 1
            tmp = 0
        elif l[a] != tmp and l[a] == 1:
            tmp = 1
print(flip)