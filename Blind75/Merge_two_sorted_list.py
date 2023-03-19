#TC:0(n)
#SC:0(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating a dummy listnode
        dummy=ListNode()
        #assigning curr variable to dummy
        curr=dummy

        #iterate until list1 and list2 exist
        while list1 and list2:
            #if the list1 value is less then list2
            if list1.val<=list2.val:
                #assign the curr's next pointer to list1
                curr.next=list1
                #move the list1 node one step
                list1=list1.next
                #update the curr pointer as curr.next
                curr = curr.next
            #if the list2 value is lesser than list1
            else:
                #assign curr's next pointer to list2
                curr.next=list2
                #move the list2 
                list2=list2.next
                #move the curr pointer as curr.next
                curr = curr.next
        
        #if the list1 or list 2 is present
        if list1 or list2:\
            #if list 1 is extra
            if list1:
                #add it to the curr.next
                curr.next = list1
                #else add the curr.next pointer to list2
            else:
                curr.next = list2
        #return the next node of dummy as we start dummy before the head       
        return dummy.next
