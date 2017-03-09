class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
