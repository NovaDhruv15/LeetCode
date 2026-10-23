class Solution:
    def sortPermutation(self, nums):
        res = -1
        for i in range(len(nums)):
            if nums[i] != i:
                res = res & nums[i]
        if res == -1:
            return 0
        return res