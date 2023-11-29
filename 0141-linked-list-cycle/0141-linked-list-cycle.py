# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        stack = []
        
        for i in range(10001):
            if head.next is None:
                return False
            elif head in stack:
                return True
            else:
                stack.append(head)
                head = head.next
        return False