class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Take the shortest string as a starting point
        mini_str = min(strs, key=len)

        for index in range(len(mini_str)):
            # Check if the current prefix is common to all strings
            for string in strs:
                if string[index] != mini_str[index]:
                    return mini_str[:index]
        
        return mini_str  # If no mismatch is found, return the entire shortest string

