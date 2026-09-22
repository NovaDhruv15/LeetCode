class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = sorted(nums1 + nums2)
        return (m[len(m) // 2] + m[(len(m) - 1) // 2]) / 2