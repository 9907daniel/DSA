# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        tmp2 = []

        while l1 != None:
            tmp.append(l1.val)
            l1 = l1.next
        while l2 != None:
            tmp2.append(l2.val)
            l2 = l2.next

        tmp.reverse(), tmp2.reverse()
        result = [0] * max(len(tmp),len(tmp2))

        for a in range(max(len(tmp),len(tmp2))):
            try:
                if tmp[a] and tmp2[a]:
                    if tmp[a]+tmp2[a] > 9:
                        result[a] = result[a]+tmp[a]+tmp2[a]-10
                        result[a+1] += 1
                    else:
                        result[a] = result[a]+tmp[a]+tmp2[a]
                print(a)
            except:
                print(a)
                if tmp[a]:
                    result[a] = result[a] + tmp[a]
                else:
                    result[a] = result[a] + tmp2[a]

        result = result[::-1]
        new_node = ListNode()
        tmp = new_node

        for a,b in enumerate(result):
            if a == len(result)-1:
                tmp.val = b
            else:
                tmp.val = b
                tmp.next = ListNode()
                tmp = tmp.next
        return new_node

