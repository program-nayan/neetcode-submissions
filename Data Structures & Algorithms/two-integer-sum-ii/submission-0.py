class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        seen = set()
        for i in range(len(numbers)):
            to_find =  target - numbers[i] 
            if to_find in seen:
                res.append(numbers.index(to_find)+1)
                res.append(i+1)
            else:
                seen.add(numbers[i])
        return res

