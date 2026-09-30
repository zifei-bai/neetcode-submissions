class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []
        for i, t in enumerate(tokens):
            if i == 0:
                stack.append(int(t))
            else:
                if t in ops:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    if t == '+':
                        result = num1 + num2
                    elif t == '-':
                        result = num1 - num2
                    elif t == '*':
                        result = num1 * num2
                    else:
                        result = math.trunc(num1 / num2)
                    stack.append(result)
                else:
                    stack.append(int(t))
            #print(stack)
        return stack[-1]
        
