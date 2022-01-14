class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        curLen, maxLen = 0, 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in seen or seen[s[j]] < i:
                curLen += 1
                seen[s[j]] = j
                j += 1
            else:
                maxLen = max(maxLen, curLen)
                i = seen[s[j]] + 1
                curLen = j - i 
        return max(maxLen, curLen)