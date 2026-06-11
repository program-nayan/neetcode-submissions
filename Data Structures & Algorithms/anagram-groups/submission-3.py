from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        res = []
        for s in strs:
            mapper["".join(sorted(s))].append(s) 
        for key,value in mapper.items():
            res.append(value)
        return res    
                                

        
