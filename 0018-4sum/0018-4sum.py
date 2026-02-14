class Solution(object):
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []
        
        nums.sort()
        result = []
        n = len(nums)
        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return []
        
        if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return []
        
        for i in range(n - 3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                needed_sum = target - nums[i] - nums[j]
                
                while left < right:
                    current_sum = nums[left] + nums[right]
                    
                    if current_sum == needed_sum:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                        
                    elif current_sum < needed_sum:
                        left += 1
                    else:
                        right -= 1
        
        return result