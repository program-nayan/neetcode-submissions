class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            if target - nums[i] in seen:
                res = [nums.index(target-nums[i]), i]
                return res
            else:
                seen.add(nums[i])