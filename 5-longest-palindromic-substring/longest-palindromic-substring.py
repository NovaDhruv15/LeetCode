class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if sub == sub[::-1] and len(sub) > len(best):
                    best = sub
        return best