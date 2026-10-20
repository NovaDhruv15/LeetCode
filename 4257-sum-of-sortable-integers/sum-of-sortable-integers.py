
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pref = [0] * (n + 1)
        suff = [float('inf')] * (n + 1)
        drop = [0] * n

        for i in range(n):
            pref[i + 1] = max(pref[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff[i] = min(nums[i], suff[i + 1])

        for i in range(1, n):
            drop[i] = drop[i - 1]
            if nums[i - 1] > nums[i]:
                drop[i] += 1

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                end = i + k - 1
                drops = drop[end] - drop[i]

                if nums[end] > nums[i]:
                    drops += 1

                if drops > 1 or pref[i] > suff[i]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans