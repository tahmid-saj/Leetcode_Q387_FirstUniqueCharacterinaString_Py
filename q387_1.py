class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = set()
        for i in range(0, len(s)):
            if i == s.rindex(s[i]) and not s[i] in prev: return i
            prev.add(s[i])
        
        return -1
