class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # here we create a dummy node to act as the head of the merged list
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If one of the lists is exhausted, attach the remaining part of the other list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
