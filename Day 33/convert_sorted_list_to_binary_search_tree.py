class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:return head
        if head.next is None:return TreeNode(head.val)
        slow,fast=head,head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        data,right,slow.next=slow.next.val,slow.next.next,None
        return TreeNode(val=data,left=self.sortedListToBST(head), 
		    right=self.sortedListToBST(right))
        
