class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in '+-*/':
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    val = int(b + a)
                    
                elif token == '-':
                    val = int(b - a)
                    
                elif token == '*':
                    val = int(b * a)
                elif token == '/':
                    import math
                    div_res = float(b)/a
                    val = math.trunc(div_res)
                stack.append(val)
                print(val)
            else:
                stack.append(int(token))
        return stack.pop()

