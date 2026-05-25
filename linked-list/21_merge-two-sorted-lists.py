"""
Problem: 21. Merge Two Sorted Lists
Pattern: Linked List
Difficulty: Easy

Key Idea:
- Compare nodes from both lists
- Attach smaller node to merged list
- Continue until both lists are exhausted

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp = ListNode()
        tail = temp

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if list1: tail.next = list1
        elif list2: tail.next = list2

        return temp.next
