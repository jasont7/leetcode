class Solution(object):
    def isAnagram(self, s, t):
        sd = {}
        for char in s:
            if char in sd:
                sd[char] += 1
            else:
                sd[char] = 1
        
        td = {}
        for char in t:
            if char in td:
                td[char] += 1
            else:
                td[char] = 1
        
        return sd == td
        