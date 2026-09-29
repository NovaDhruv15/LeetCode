class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        b = [[] for _ in range(26)]
        for w in words:
            it = iter(w)
            b[ord(next(it)) - 97].append(it)
            
        ans = 0
        for c in s:
            old, b[ord(c) - 97] = b[ord(c) - 97], []
            for it in old:
                nxt = next(it, None)
                if nxt:
                    b[ord(nxt) - 97].append(it)
                else:
                    ans += 1
                    
        return ans