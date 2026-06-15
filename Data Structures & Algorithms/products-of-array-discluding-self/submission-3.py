import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1]*len(nums)
        suffix_prod = [1]*len(nums)
        res = []
        for i in range(len(nums)):
            if i == 0:
                pref_prod[i] = nums[i]
            else:
                pref_prod[i] = nums[i] * pref_prod[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix_prod[i] = nums[i]
            else:
                suffix_prod[i] = nums[i] * suffix_prod[i+1]
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_prod[i+1])
            elif i == len(nums)-1:
                res.append(pref_prod[i-1])
            else:
                res.append(pref_prod[i-1] * suffix_prod[i+1])
        return res
