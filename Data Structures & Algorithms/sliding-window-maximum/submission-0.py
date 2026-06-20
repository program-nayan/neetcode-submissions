class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        right  = left+k
        while right<len(nums)+1:
            res.append(max(nums[left:right]))
            left += 1
            right += 1
        return res