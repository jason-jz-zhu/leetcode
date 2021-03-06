class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2

        start, end = 0, n1
        while start < end:
            m1 = start + (end - start) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                start = m1 + 1
            else:
                end = m1

        m1 = end
        m2 = k - end

        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1],
                float('-inf') if m2 <= 0 else nums2[m2 - 1])

        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],
                float('inf') if m2 >= n2 else nums2[m2])

        return (c1 + c2) / 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left_idx, right_idx = (m + n + 1) // 2, (m + n + 2) // 2
        left_val = self.find_kth(nums1, 0, nums2, 0, left_idx)
        right_val = self.find_kth(nums1, 0, nums2, 0, right_idx)
        return (left_val + right_val) / 2

    def find_kth(self, nums1, idx1, nums2, idx2, k):
        if idx1 >= len(nums1):
            return nums2[idx2 + k - 1]
        if idx2 >= len(nums2):
            return nums1[idx1 + k - 1]
        if k == 1:
            return min(nums1[idx1], nums2[idx2])
        val1 = idx1 + k // 2 - 1 if idx1 < len(nums1) else float('-inf')
        val2 = idx2 + k // 2 - 1 if idx2 < len(nums2) else float('-inf')
        if val1 < val2:
            return self.find_kth(nums1, idx1 + k // 2, nums2, idx2, k - k // 2)
        else:
            return self.find_kth(nums1, idx1, nums2, idx2 + k // 2, k - k // 2)


class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        size = len(nums1) + len(nums2)
        smaller = self.find_kth(nums1, nums2, (size + 1) // 2)
        bigger = self.find_kth(nums1, nums2, (size + 2) // 2)
        return (smaller + bigger) / 2

    def find_kth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        v1 = nums1[k // 2 - 1] if k // 2 - 1 < len(nums1) else float('inf')
        v2 = nums2[k // 2 - 1] if k // 2 - 1 < len(nums2) else float('inf')
        if v1 < v2:
            return self.find_kth(nums1[k // 2: ], nums2, k - k // 2)
        else:
            return self.find_kth(nums1, nums2[k // 2: ], k - k // 2)
