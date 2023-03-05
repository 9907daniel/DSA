# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        tmp = []
        copied = head
        copied_new_node = new_node

        if head == None:
            return head

        while copied:
            tmp.append(copied.val)
            copied = copied.next

        for b,a in enumerate(tmp[::-1]):
            copied_new_node.val = a
            if b != len(tmp)-1:
               copied_new_node.next = ListNode()
            copied_new_node = copied_new_node.next
        return new_node