"""
Problem: 206. Reverse Linked List
Pattern: Linked List
Difficulty: Easy

Key Idea:
- Reverse pointers one by one
- Track previous and next nodes
- Move through list iteratively

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        current = head

        prev, next = None, None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev