class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        c = 0
        
        while l1 or l2 or c:
            if l1: c += l1.val; l1 = l1.next
            if l2: c += l2.val; l2 = l2.next
            
            cur.next = cur = ListNode(c % 10)
            c //= 10
            
        return dummy.next