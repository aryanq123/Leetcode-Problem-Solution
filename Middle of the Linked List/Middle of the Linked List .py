# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=dummy.next
        fast=slow.next
        count=0
        while dummy:
            dummy=dummy.next
            count+=1
            

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow if count % 2==0 else slow.next

        
