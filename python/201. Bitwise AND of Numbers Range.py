class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0

        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
