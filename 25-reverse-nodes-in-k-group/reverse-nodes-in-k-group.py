class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Step 1: check if k nodes exist
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Step 2: reverse k nodes
            group_next = kth.next
            prev = group_next
            curr = prev_group.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 3: reconnect
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp
