class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        res = [0]*len(temperatures)
        for ind, temp in enumerate(temperatures):
            while temp_stack and temp>temp_stack[-1][0]:
                temp_stack_t, temp_stack_i = temp_stack.pop()
                res[temp_stack_i] = ind - temp_stack_i
            temp_stack.append((temp, ind))
        return res



        