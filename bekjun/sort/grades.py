
n = int(input())
dic = []
for a in range(n):
    data = input().split()
    dic.append(data[0], int(data[1]))
    
sorted_array = sorted(dic, key=lambda student:student[1])

for student in sorted_array:
    print(student[0])


