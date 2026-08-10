class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # b // a is not correct when a or b is negetive ! (The division between two integers always truncates toward zero.)
            else:
                stack.append(int(t))
            # print(f"t:{t} stack:{stack}")
            
        return stack[0] 