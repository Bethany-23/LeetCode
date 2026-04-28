class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find length and tail
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Make it circular
        tail.next = head
        
        # 3. Reduce k
        k = k % length
        
        # 4. Find new tail (length - k - 1 steps)
        steps_to_new_tail = length - k - 1
        new_tail = head
        
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # 5. New head
        new_head = new_tail.next
        
        # 6. Break the cycle
        new_tail.next = None
        
        return new_head