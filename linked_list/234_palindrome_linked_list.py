# Given the head of a singly linked list, return true if it is a 
# palindrome
# or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Solving using Brute Linked List
        while head != None:
            if head.next == None:
                return True
            tail = head
            while tail.next != None:
                tail = tail.next
            if head.val == tail.val:
                remove_last = head
                while remove_last.next.next != None:
                    remove_last = remove_last.next
                remove_last.next = None
                head = head.next
            else: 
                return False
        return True
            

        # Using Normal List       
        while head != None:
            l.append(head.val)
            head = head.next
        
        start = 0
        end = len(l)-1

        while start <= end:
            if l[start] == l[end]:
                start += 1
                end -= 1
            else:
                return False
        return True