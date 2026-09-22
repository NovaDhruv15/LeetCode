class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m=0
        nums1=nums1+nums2
        n=len(nums1)
        nums1.sort()
        if n%2==0:
             m=m+(nums1[n//2]+ nums1[n//2-1])/2
        else:
            m=m+nums1[n//2]
        return m
