from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        res = []
        arr = []
        for key,value in hashmap.items():
            arr.append((key, value))
        arr.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(arr[i][0])
        return res

        



