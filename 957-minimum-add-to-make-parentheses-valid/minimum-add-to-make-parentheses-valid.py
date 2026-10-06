class Solution:
    def minAddToMakeValid(self, s):
        first_list = 0
        last_list = 0

        for char in s:
            if char == '(':
                first_list += 1
            elif first_list > 0:
                first_list -= 1
            else:
                last_list += 1

        return last_list + first_list