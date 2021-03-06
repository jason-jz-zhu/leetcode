class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        s, res = 0, -sys.maxint - 1
        hashmap = {}
        for i in xrange(len(nums)):
            s += nums[i]
            if s == k:
                res = i + 1
            elif s - k in hashmap:
                res = max(res, i - hashmap[s - k])
            if s not in hashmap:
                hashmap[s] = i
        if res == -sys.maxint - 1:
            return 0
        return res
