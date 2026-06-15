import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        mid = nums.copy()
        res = []
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(int(product/nums[i]))
            else:
                del mid[i]
                res.append(math.prod(mid))
                mid = nums.copy()
        return res
