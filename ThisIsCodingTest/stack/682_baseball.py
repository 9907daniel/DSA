# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_list = []

        for a in operations:
            if a == "C":
                new_list.pop()
            elif a =="D":
                new_list.append(int(new_list[-1])*2)
            elif a =="+":
                new_list.append(int(new_list[-1])+int(new_list[-2]))
            else:
                new_list.append(int(a))
            print(new_list)
        return sum(new_list)

# BigO(N)