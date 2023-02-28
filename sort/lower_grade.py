n = int(input())
listed = []

for a in range(n):
    input_data = input().split()
    listed.append((input_data[0], int(input_data[1])))
    
print(listed)

for i in range(n):
    listed = sorted(listed, key=lambda student: student[1])
    
for student in listed:
    print(student[0], end= ' ')