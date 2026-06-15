import math
class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ''.join(f'{len(s)}#{s}' for s in strs)
        return temp
                
    def decode(self, s: str) -> List[str]:
        res = []    
        i = 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j+=1
            len_of_str = int(s[i:j])
            word = s[j+1:j+1+len_of_str]
            res.append(word)
            i = j+1+len_of_str
        return res



