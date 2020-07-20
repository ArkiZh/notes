"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""

class Solution:
    def wordBreak(self, s, wordDict):
        if s==None or len(s)==0 or wordDict==None or len(wordDict)==0:
            return False
        len_s = len(s)
        dp = [False]*(len_s+1)
        dp[0]=True
        for i in range(1,len_s+1):
            for word in wordDict:
                pre = i-len(word)
                if pre>=0 and dp[pre] and s[pre:i]==word:
                    dp[i]=True
                    break
        return dp[-1]

print(Solution().wordBreak("applepenapple", wordDict = ["apple", "pen"]))
