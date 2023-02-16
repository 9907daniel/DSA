# Solution using fast & slow two pointers

class Solution(object):
    def isPalindrome(self, head):
        prev = adva = head

        # Step 1
        while adva and adva.next:
           adva = adva.next.next
           prev = prev.next
        
        # Step 2
        list1, list2 = [], []
        adva = prev 
        prev = head
        while adva:
            list2.append(prev.val)
            list1.append(adva.val)
            adva = adva.next
            prev = prev.next

        # Step 3
        list2.reverse()
        return list1 == list2




