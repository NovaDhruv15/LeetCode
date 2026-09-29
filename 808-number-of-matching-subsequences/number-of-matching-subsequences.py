class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            offset = 0
            for c in word:
                offset = s.find(c, offset)
                if offset == -1:
                    break
                offset += 1
            if offset != -1:
                count += 1
        return count
        