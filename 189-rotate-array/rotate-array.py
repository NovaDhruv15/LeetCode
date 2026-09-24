class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        if k:
            # 1. In-place C-optimized reverse of the whole list
            nums.reverse()
            
            # 2. Reverse the first k elements using an iterator (avoids list concatenation)
            nums[:k] = reversed(nums[:k])
            
            # 3. Reverse the remaining elements
            nums[k:] = reversed(nums[k:])