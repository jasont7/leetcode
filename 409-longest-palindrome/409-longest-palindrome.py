class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        maxlen = 0
        for char in list(d):
            if d[char] >= 2:
                
                maxlen += d[char] if d[char] % 2 == 0 else d[char] - 1
                d[char] -= d[char] if d[char] % 2 == 0 else d[char] - 1
                if d[char] == 0:
                    d.pop(char)
        
        if len(d): maxlen += 1
        return maxlen