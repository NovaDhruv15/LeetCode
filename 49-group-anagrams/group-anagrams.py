class Solution:
    def groupAnagrams(self, strs):
        ans = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in ans:
                ans[key] = []

            ans[key].append(s)

        return list(ans.values())