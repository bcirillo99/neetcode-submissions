class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        for t in tokens:
            if t in op_map:
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(op_map[t](first_num,second_num))
            else:
                stack.append(int(t))
        return stack[0]
