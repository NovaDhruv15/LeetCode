class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = 0
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        return res