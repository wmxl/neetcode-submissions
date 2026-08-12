class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        def match(c1, c2):
            if c1 == '(':
                return c2 == ')'
            if c1 == '{':
                return c2 == '}'
            if c1 == '[':
                return c2 == ']'
            
        stack = []
        for c in s:
            if stack and match(stack[-1], c):
                stack.pop()
            
            else: stack.append(c)

        return len(stack) == 0



        