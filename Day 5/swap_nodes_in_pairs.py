class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next
            first.next = second.next
            current.next = second
            current.next.next = first
            current = current.next.next
        return dummy.next
