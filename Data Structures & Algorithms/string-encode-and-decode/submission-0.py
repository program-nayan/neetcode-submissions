import math
class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ''
        for i in range(len(strs)):
            if not strs[i]:
                pass
            else:
                for letter in strs[i]:
                    num = ord(letter)*2 + 13
                    temp += chr(num)
            temp += '_|$|_'
        return temp
                
    def decode(self, s: str) -> List[str]:
        res = s.split('_|$|_')
        final = []
        for i in range(len(res)):
            if not res[i]:
                final.append('')
            else:
                currword = ''
                for letter in res[i]:
                    num = int((ord(letter) - 13) / 2)
                    currword += chr(num)
                final.append(currword)
        final.pop()
        return final

