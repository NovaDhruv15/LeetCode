class Solution:
    def groupAnagrams(self, strs):
        ans = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in ans:
                ans[key] = []

            ans[key].append(s)

        return list(ans.values())