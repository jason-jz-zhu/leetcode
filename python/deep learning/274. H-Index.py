# O(n)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            if c < n:
                cnt[c] += 1
            else:
                cnt[n] += 1

        t = 0
        for i in xrange(n, -1, -1):
            t += cnt[i]
            if t >= i:
                return i
        return 0

# O(nlogn)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        citations.sort()
        i = 0
        size = len(citations)
        while i < size and citations[size-1-i] > i:
            i += 1
        return i

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0
        return max([min(len(citations) - i, c) for i, c in enumerate(sorted(citations))])
