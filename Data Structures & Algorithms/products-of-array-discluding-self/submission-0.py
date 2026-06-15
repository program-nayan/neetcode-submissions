import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        mid = nums.copy()
        for i in range(len(nums)):           
            del mid[i]
            res.append(math.prod(mid))
            mid.insert(i, nums[i])
        return res
