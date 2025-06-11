class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        l1, l2 = headA, headB
        
        while l1:
            lenA += 1
            l1 = l1.next
            
        while l2:
            lenB += 1
            l2 = l2.next
        
        l1, l2 = headA, headB
        
        diff = abs(lenA - lenB)
        
        if lenA > lenB:
            for _ in range(diff):
                l1 = l1.next
        else:
            for _ in range(diff):
                l2 = l2.next
                
        while l1 and l2:
            if l1 == l2:
                return l1
            l1 = l1.next
            l2 = l2.next