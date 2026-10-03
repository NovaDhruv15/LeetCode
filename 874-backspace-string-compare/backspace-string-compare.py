class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string : str) -> list[str]:
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        return build(s) == build(t)
                