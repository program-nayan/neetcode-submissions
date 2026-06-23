class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {"(":")","[":"]","{" :"}"}
        opened_seq = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] in p_dict:
                opened_seq.append(s[i])
            else:
                if not opened_seq or p_dict[opened_seq[-1]] != s[i]:
                        return False
                opened_seq.pop()
        return len(opened_seq) == 0