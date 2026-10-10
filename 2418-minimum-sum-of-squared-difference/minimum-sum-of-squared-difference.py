class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        MAX_D = 100000
        freq = [0] * (MAX_D + 1)
        maxDiff = 0
        totalDiff = 0

        # Step 1: Calculate differences and frequencies
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            freq[d] += 1
            totalDiff += d
            if d > maxDiff:
                maxDiff = d

        # Step 2: Combine operations
        k = k1 + k2

        # Step 3: Check if all differences can become zero
        if totalDiff <= k:
            return 0

        # Step 4: Reduce the largest differences first
        d = maxDiff
        while d > 0 and k > 0:
            moves = min(k, freq[d])
            freq[d] -= moves
            freq[d - 1] += moves
            k -= moves
            d -= 1

        # Step 5: Calculate the final squared sum
        return sum(i * i * f for i, f in enumerate(freq) if f)