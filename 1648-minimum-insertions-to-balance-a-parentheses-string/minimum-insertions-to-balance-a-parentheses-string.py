class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        operations = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                balance += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    operations += 1
                if balance > 0:
                    balance -= 1
                else:
                    operations += 1
            i += 1
        operations += balance * 2
        return operations 