class Solution(object):
    def countLargestGroup(self, n):
        count = {}  # Use a regular dictionary

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            if digit_sum in count:
                count[digit_sum] += 1
            else:
                count[digit_sum] = 1

        max_size = max(count.values())
        largest_group_count = 0

        for value in count.values():
            if value == max_size:
                largest_group_count += 1

        return largest_group_count
