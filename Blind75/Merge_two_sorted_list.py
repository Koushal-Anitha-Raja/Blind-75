class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy

        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
                curr = curr.next
            else:
                curr.next=list2
                list2=list2.next
                curr = curr.next
        
        if list1 or list2:
            if list1:
                curr.next = list1
            else:
                curr.next = list2
                
        return dummy.next
