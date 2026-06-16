class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(char for char in s if char.isalnum())
        return new_str.lower() == new_str[::-1].lower()
        