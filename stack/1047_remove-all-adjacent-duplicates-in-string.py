"""
Problem: 1047. Remove All Adjacent Duplicates In String
Pattern: Stack
Difficulty: Easy

Key Idea:
- Use stack to track characters
- Remove top if duplicate appears
- Build final string from stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def removeDuplicates(self, s):
        stack = []

        for char in s:
            top = stack[-1] if stack else None

            if char == top:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
            