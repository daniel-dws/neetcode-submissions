class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        d = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())

