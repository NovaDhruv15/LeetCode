class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        square = [x * x for x in nums]
        square.sort()
        score = 0
        for i in range(n//2):
            score -= square[i]
        for i in range(n//2, n):
            score += square[i]
        return score 