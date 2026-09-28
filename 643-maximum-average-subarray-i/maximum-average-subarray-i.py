class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k])
        M = avg
        for i in range(k,len(nums)):
            avg = avg - nums[i-k] + nums[i]
            if avg>M:
                M=avg
        return M/k



        