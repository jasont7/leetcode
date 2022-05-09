class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_chars = {}
        for c in magazine:
            if c in magazine_chars:
                magazine_chars[c] += 1
            else:
                magazine_chars[c] = 1
        
        for c in ransomNote:
            if c in magazine_chars and magazine_chars[c] > 0:
                magazine_chars[c] -= 1
            else:
                return False
        return True