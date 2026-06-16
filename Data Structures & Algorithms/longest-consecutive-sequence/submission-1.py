class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            unique_nums = list(set(nums))
            unique_nums.sort()
            count = 1
            max_len = 1
            for i in range(len(unique_nums)-1):
                if unique_nums[i+1] == unique_nums[i]+1:
                    count += 1
                    max_len = max(max_len, count)
                else:
                    count = 1
            return max_len


        