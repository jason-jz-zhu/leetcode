class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        for c in t:
            if s[i] == c:
                i += 1
            if i == len(s):
                break
        return i == len(s)
