class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Traverse through list
        front = 0
        back = len(heights) - 1
        max_area = min(heights[front], heights[back]) * back
        while front < back:
            height = min(heights[front], heights[back]) 
            width = back - front
            area = height * width
            if heights[front] < heights[back]:
                front += 1
            else:
                back -= 1

            if area > max_area:
                max_area = area
        return max_area
            

        