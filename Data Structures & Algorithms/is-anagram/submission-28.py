class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution3
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_s[ord(t[i]) - ord('a')] -= 1
        return all(val == 0 for val in count_s)

        