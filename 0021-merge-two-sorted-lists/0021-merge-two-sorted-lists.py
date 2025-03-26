# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            result = list1
            cur_1 = list1.next
        else:
            result = list2
            cur_2 = list2.next
        
        head = result

        while cur_1 is not None and cur_2 is not None:
            if cur_1.val <= cur_2.val:
                result.next = cur_1
                cur_1 = cur_1.next
            else:
                result.next = cur_2
                cur_2 = cur_2.next
            result = result.next

        if cur_1 is None:
            result.next = cur_2
        else:
            result.next = cur_1
        return head