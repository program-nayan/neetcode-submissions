import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        num_stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ops:
                num_stack.append(int(tokens[i]))
            else:
                op = ops[tokens[i]]
                second_num = num_stack.pop()
                first_num = num_stack.pop()
                num_stack.append(int((op)(first_num, second_num)))
       
        return num_stack[-1]