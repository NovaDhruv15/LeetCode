class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        arr = sorted(nums)
        ans = []

        for num in nums:
            count = 0

            for i in range(len(arr)):
                if arr[i] >= num:
                    break
                count += 1
            ans.append(count)
        return ans
