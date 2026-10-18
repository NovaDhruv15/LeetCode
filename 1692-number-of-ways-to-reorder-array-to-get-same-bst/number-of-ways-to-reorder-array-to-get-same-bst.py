import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def count_ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            combinations = math.comb(len(left) + len(right), len(left))
            left_ways = count_ways(left)
            right_ways = count_ways(right)
            return (combinations * left_ways * right_ways) % MOD
        return (count_ways(nums) - 1) % MOD