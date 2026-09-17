class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = sorted(list(s))
        lt = sorted(list(t))

        for i in range(len(s)):
            if ls[i] != lt[i]:
                return False
        return True
        