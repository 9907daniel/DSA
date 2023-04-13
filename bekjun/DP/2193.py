n = int(input())

binary = bin(n)[2:]
bits = [int(bit) for bit in binary]
d = [0]*91

count = 0






# for i in range(len(bits)):
#     if bits[i] == 1:
#         if i != (len(bits)-1):
#             if bits[i+1] != 1:
#                 count += 1
#         if i == (len(bits)-1) and bits[i] == 1:
#             count += 1
    
# print(count)
            