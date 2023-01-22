list = [7, 4, 5, 4, 6]


class BigNumberLaw():

  def law(n=5, m=8, k=3):
    list.sort()
    count = 0
    count_consecutive = 0
    total = 0

    print(list)

    while count < m:
      if count_consecutive < k:
        total = total + list[-1]
        count += 1
      else:
        total = total + list[-2]
        count += 1

    print(total)


BigNumberLaw.law()

# Time : 17 minute
# No implementation of inputting integers.
# Time Complexity : O(n)
