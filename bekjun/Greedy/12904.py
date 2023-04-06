s = list(input())
t = list(input())

check = False
while len(s) < len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if t == s:
        check = True
        
if check:
    print(1)
else:
    print(0)


# def game(s,t):
#     while len(s) < len(t):
#         if s == t:
#             return True
#         s1 = s[:]+['A']
#         if game(s1,t):
#             return True
#         s2 = s[:]
#         s2.reverse()
#         s2 = s2 + ['B']
#         if game(s2,t):
#             return True
        
#         return False
    
# if game(s,t):
#     print(1)
# else:
#     print(0)
