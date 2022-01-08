class Solution(object):
    def maxArea(self, lines):
        maxVol = 0
        l, r = 0, len(lines)-1
        while l < r:
            curVol = min(lines[l], lines[r]) * (r-l)
            maxVol = max(maxVol, curVol)
            if lines[l] < lines[r]:
                l += 1
            else:
                r -= 1
        return maxVol