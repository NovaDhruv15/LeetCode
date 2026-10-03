class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = [-1] * 10001
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smallest_number = stack.pop()
                next_greater[smallest_number] = num
            stack.append(num)
        return [next_greater[num] for num in nums1]