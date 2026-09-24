class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
            
        k = k % n
        if k == 0:
            return
            
        # Modifies the original array in-place using C-optimized slicing
        nums[:] = nums[-k:] + nums[:-k]