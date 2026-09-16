class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = "".join([char.lower() for char in s if char.isalnum()])

        for i in range(len(l) // 2):
            if l[i] != l[(len(l) - i -1)]:
                return False
        return True
        