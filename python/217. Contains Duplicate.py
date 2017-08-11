class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        counter = collections.Counter(nums)
        return sum([1 for val in counter.values() if val > 1]) > 0


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        # init hash
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        # scan hash
        for key, value in hash.iteritems():
            if value >= 2:
                return True

        return False
