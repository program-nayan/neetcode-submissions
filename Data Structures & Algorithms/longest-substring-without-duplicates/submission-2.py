class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = i+1
        max_len = 0
        if len(s)<2:
            return len(s)
        
        seen  = {s[0]}
        while j<len(s):
            if s[j] in seen:
                i += 1
                j = i+1
                seen.clear()
                seen.add(s[i])
                
            else:
                seen.add(s[j])
                j += 1
            max_len = max(max_len, len(seen))
        return max_len