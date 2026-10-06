class Solution:
    def minAddToMakeValid(self, s):
        open_needed = 0
        additions = 0

        for char in s:
            if char == '(':
                open_needed += 1
            elif open_needed > 0:
                open_needed -= 1
            else:
                additions += 1

        return additions + open_needed