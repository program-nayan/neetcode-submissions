from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        res = []
        hash_arr = []
        for key, val in hashmap.items():
            hash_arr.append((key,val))
        for i in range(len(hash_arr)-k):
            hash_arr.remove(min(hash_arr, key=lambda x: x[1]))

        for i in range(k):
            res.append(hash_arr[i][0])
        return res
            
