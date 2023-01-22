
amount = 1300
list = [500,100,50,10]
count = 0

for coins in list:
  amount % coins  
  count += 1
  
print(count)

# time complexity : O(n) : depends on the number of types of coins not
# Greedy is not a viable solution in most algorithms 



