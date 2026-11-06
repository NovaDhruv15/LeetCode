class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        # pair each query with its original position, then sort
        qs = []
        for i in range(len(queries)):
            qs.append((queries[i], i))
        qs.sort()

        count = [0] * (n + 1)
        active = 0
        left = 0
        right = 0
        ans = [0] * len(queries)

        for q, i in qs:
            # add logs with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if count[server] == 0:
                    active += 1
                count[server] += 1
                right += 1

            # remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                count[server] -= 1
                if count[server] == 0:
                    active -= 1
                left += 1

            ans[i] = n - active

        return ans