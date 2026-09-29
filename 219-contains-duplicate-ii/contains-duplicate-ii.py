class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indexed_nums = [(nums, i ) for i, nums in enumerate(nums)]
        indexed_nums.sort()
        for i in range (1, len(indexed_nums)):
            if indexed_nums[i][0] == indexed_nums[i-1][0]:
                if indexed_nums[i][1] - indexed_nums[i-1][1] <= k:
                    return True
        return False