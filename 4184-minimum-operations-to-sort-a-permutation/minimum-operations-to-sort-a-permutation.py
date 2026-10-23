class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        z = nums.index(0)
        ans = float('inf')
        if all(nums[(z + i) % n ] == i for i in range(n)):
            ans = min(ans, z ,n - z + 2)
        if all(nums[(z - i) % n ] == i for i in range(n)):
            ans = min(ans, z + 2, n - z)
        return -1 if ans == float('inf') else ans