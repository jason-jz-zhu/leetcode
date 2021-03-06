class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        if dict is None or len(dict) == 0:
            return s

        check = [0] * len(s)
        for d in dict:
            pos = s.find(d)
            while pos != -1:
                check[pos: pos + len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)

        res, pre = [], 0
        for i in range(len(s)):
            if pre != check[i]:
                res += '</b>' if pre else '<b>'
                pre = check[i]
            res += s[i]
        if pre:
            res += '</b>'

        return ''.join(res)
