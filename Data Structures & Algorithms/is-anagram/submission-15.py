class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        list_s = list(s)
        list_t = list(t)
        if len(list_s) == len(list_t):
            for char in list_s:
                dict_s[char] = dict_s.get(char, 0) + 1
            for char in list_t:
                dict_t[char] = dict_t.get(char, 0) + 1   
            return (dict_s == dict_t)
        return False
