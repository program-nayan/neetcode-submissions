from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = Counter(s1)
        hash_s2 = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)+1):
            if hash_s2 == hash_s1:
                return True
            else:
                hash_s2[s2[i]] -= 1
                if hash_s2[s2[i]] == 0:
                    hash_s2.pop(s2[i], None)
                if i+len(s1)< len(s2):
                    hash_s2[s2[i+len(s1)]] = 1 + hash_s2.get(s2[i+len(s1)], 0)
        return False


        