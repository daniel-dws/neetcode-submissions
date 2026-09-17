class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        count = 0
        highest = 0

        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        start = None
        for key in d:
            if d.get(key - 1) is None:
                start = key
                count = 1
                while d.get(start+1) is not None:
                    count += 1
                    start += 1
                highest = max(count, highest)

        return highest
