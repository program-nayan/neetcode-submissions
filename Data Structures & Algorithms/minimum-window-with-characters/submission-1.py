from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not s or not t:
            return ""

        left = 0
        need = Counter(t)
        have = {}
        got = 0
        required = len(need)
        min_size = float('inf')
        res_left = 0 

        for right in range(len(s)):
            char = s[right]
            have[char] = 1 + have.get(char, 0)

            if char in need and have[char] == need[char]:
                got += 1

            while got == required:
                left_char = s[left]
     
                if (right - left + 1) < min_size:
                    min_size = right - left + 1
                    res_left = left 

                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    got -= 1
                
                left += 1
        
        return s[res_left : res_left + min_size] if min_size != float('inf') else ""