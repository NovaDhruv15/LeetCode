class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for u, v in edges: g[u].append(v); g[v].append(u)
        ch = [ord(c) - 97 for c in s]
        tin, tout, pre, up = [0]*n, [0]*n, [1 << ch[0]] + [0]*(n-1), [[0]*n]
        tin[0] = t = 1
        st = [(0, iter(g[0]))]
        while st:
            u, it = st[-1]
            for v in it:
                if not tin[v]:
                    t += 1; tin[v] = t; up[0][v] = u; pre[v] = pre[u] ^ 1 << ch[v]
                    st.append((v, iter(g[v]))); break
            else: tout[u] = t; st.pop()
        for _ in range(n.bit_length()): up.append([up[-1][up[-1][x]] for x in range(n)])
        anc = lambda x, y: tin[x] <= tin[y] <= tout[x]
        def lca(a, b):
            if anc(a, b): return a
            for r in reversed(up):
                if not anc(r[a], b): a = r[a]
            return up[0][a]
        bit = [0] * (n + 2)
        def upd(i, x):
            while i <= n + 1: bit[i] ^= x; i += i & -i
        def cur(x):
            r, i = pre[x], tin[x]
            while i: r ^= bit[i]; i &= i - 1
            return r
        ans = []
        for q in queries:
            o, a, b = q.split(); u = int(a)
            if o == "update":
                c = ord(b) - 97; d = 1 << ch[u] ^ 1 << c; ch[u] = c
                upd(tin[u], d); upd(tout[u] + 1, d)
            else:
                v = int(b); m = cur(u) ^ cur(v) ^ 1 << ch[lca(u, v)]
                ans.append(not m & m - 1)
        return ans