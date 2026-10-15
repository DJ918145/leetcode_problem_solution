class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)

        if k == n:
            return max(nums)

        if k == 1:
            candidates = [
                num for num in set(nums)
                if nums.count(num) == 1
            ]
            return max(candidates) if candidates else -1

        first = nums[0]
        last = nums[-1]

        first_unique = nums.count(first) == 1
        last_unique = nums.count(last) == 1

        if first_unique and last_unique:
            return max(first, last)
        elif first_unique:
            return first
        elif last_unique:
            return last

        return -1