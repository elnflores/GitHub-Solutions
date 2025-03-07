class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        left = height[0]
        right = height[len(height) - 1]
        
        for i in range(len(height)):
            max_left[i] = left
            if height[i] > left:
                left = height[i]
            i += 1
        
        for j in range(len(height) - 1, 0, -1):
            max_right[j] = right
            if height[j] > right:
                right = height[j]
            j -= 1
        
        vol = 0
        for i in range(len(height)):
            if min(max_left[i], max_right[i]) - height[i] >= 0:
                vol += min(max_left[i], max_right[i]) - height[i]
        
        return vol