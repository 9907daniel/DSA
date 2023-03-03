# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# eX) Input: head = [1,2,3,4,5,6]
#     Output: [4,5,6]

# BigO(n)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointers that go the different speed
        first_pointer = head
        second_pointer = head

        while second_pointer.next:
            if second_pointer.next.next is None:
                second_pointer = second_pointer.next
            else:
                second_pointer = second_pointer.next.next
            first_pointer = first_pointer.next
        return first_pointer
    
