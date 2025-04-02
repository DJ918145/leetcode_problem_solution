class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pointer to track the position of valid elements
        write_index = 0
        
        # Iterate through the list to allow at most two occurrences
        for num in nums:
            if write_index < 2 or nums[write_index - 2] != num:
                nums[write_index] = num
                write_index += 1

        return write_index