class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLen = 0
        curLen = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in seen:
                curLen += 1
                seen[s[j]] = j
                j += 1
            else:
                maxLen = max(maxLen, curLen)
                k = True
                while k:
                    if s[i] == s[j]:
                        k = False
                    seen.pop(s[i])
                    i += 1
                    curLen -= 1
        return max(maxLen, curLen)