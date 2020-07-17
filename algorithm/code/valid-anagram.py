"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = dict()
        for c in s:
            m[c] = m.get(c)+1 if c in m else 1
        for c in t:
            temp = m.get(c)
            if temp is None:
                return False
            else:
                if temp == 1:
                    del m[c]
                else:
                    m[c] = temp-1
        return len(m) == 0

s = "anagram"
t = "anagram"
print(Solution().isAnagram(s,t))
