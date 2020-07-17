"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False
        pairs = {")":"(","}":"{","]":"["}
        stack = []
        for c in s:
            if c in pairs:
                # Should check whether stack is empty
                if not stack or pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack


if __name__=="__main__":
    s = "()"
    print(Solution().isValid(s))
