# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=fast=head
        if not head:
            return
        while(fast and fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                slow=head
                
                while(slow is not fast):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None 
        
