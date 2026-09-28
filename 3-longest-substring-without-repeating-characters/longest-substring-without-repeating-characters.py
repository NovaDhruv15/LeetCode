class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1]*128
        max_length = 0
        start = 0
        for end in range(len(s)):
            char_idx = ord(s[end])
            if last_seen[char_idx] >= start:
                start = last_seen[char_idx] + 1
            last_seen[char_idx] = end
            max_length = max(max_length, end - start + 1)
        return max_length