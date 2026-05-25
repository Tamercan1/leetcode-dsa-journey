"""
Problem: 20. Valid Parentheses
Pattern: Stack
Difficulty: Easy

Key Idea:
- Push opening brackets into stack
- Match closing brackets with stack top
- Stack must be empty at the end

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for ch in s:
            if ch in "])}":
                top = stack.pop() if stack else None

                if mapping[ch] != top:
                    return False
            
            else:
                stack.append(ch)

        return not stack