class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # 1. Find the middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list
        curr = slow.next
        slow.next = None

        # 3. Reverse the second half
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 4. Merge the two halves
        left, right = head, prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next