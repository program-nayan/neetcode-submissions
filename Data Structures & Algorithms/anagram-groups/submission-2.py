from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        new_strs = []
        if len(strs) == 1:
            return [strs]
        for i in range(len(strs)):
            new_strs.append((i, sorted(strs[i])))
        new_strs.sort(key=lambda x: x[1])
        mid = []
        for i in range(len(new_strs)-1):
            mid.append(strs[new_strs[i][0]])
            if i == len(new_strs)-2:
                if new_strs[i][1] != new_strs[i+1][1]:
                    res.append(mid)
                    res.append([strs[new_strs[i+1][0]]])
                else:
                    mid.append(strs[new_strs[i+1][0]])
                    res.append(mid)
            elif new_strs[i][1] != new_strs[i+1][1]:
                res.append(mid)
                mid = []
            else:
                continue
            
        return res
                                

        
