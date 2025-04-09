class Solution(object):
    def findMaxAverage(self, nums, k):
        # Initialize the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return float(max_sum) / k