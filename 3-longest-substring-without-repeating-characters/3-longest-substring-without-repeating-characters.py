class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        curlen = maxlen = 0
        left = right = 0
        while right < len(s):
            if s[right] not in seen or seen[s[right]] < left:
                seen[s[right]] = right
                curlen += 1
                right += 1
            else:
                maxlen = max(maxlen, curlen)
                left = seen[s[right]] + 1
                curlen = right - left
        return max(maxlen, curlen)