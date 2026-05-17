class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while tokens:
            item = tokens.pop(0)
            if item not in ['+','-','*','/']:
                stack.append(int(item))
            else:
                ops = item
                second = stack.pop()
                first = stack.pop()
                if ops =='+':
                    first = first + second
                elif ops =='-':
                    first = first - second
                elif ops =='*':
                    first = first * second
                elif ops =='/':
                    first = first / second
                stack.append(int(first))

        return stack[0]
