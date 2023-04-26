n = input()
l = [a for a in n]


current = '+'
not_number = ['-','+']
total_count = 0
current_number = '0'
for a in range(len(l)):
    if l[a] not in not_number:
        current_number = current_number + l[a]
        if a == len(l)-1:
            if current == '+':
                total_count += int(current_number)
            else:
                total_count -= int(current_number)

    else:
        
        if current == '-':
            total_count -= int(current_number)
            current_number = ''
        else:
            total_count += int(current_number)
            current_number = ''
        
        if l[a] == '-' and current == '+':
            current = '-'
            
        elif l[a] == '-' and current == '-':
            current = '-'
            
        elif l[a] == '+' and current == '-':
            current = '-'
        
        elif l[a] == '+' and current == '+':
            current = '+'


print(total_count)