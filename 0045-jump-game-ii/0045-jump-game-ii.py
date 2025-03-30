class Solution:
    def jump(self, nums):
        jumps = 0
        max_reach = 0
        jump_end = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == jump_end:  
                jumps += 1  
                jump_end = max_reach  

                if jump_end >= len(nums) - 1:
                    return jumps  

        return jumps
