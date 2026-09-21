# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        cur = head

        while cur:
            if cur in d:
                return True
            d[cur] = True 
            cur = cur.next
        return False

            