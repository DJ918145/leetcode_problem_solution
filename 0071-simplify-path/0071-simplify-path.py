class Solution(object):
    def simplifyPath(self, pat):
        """
        :type path: str
        :rtype: str
        """
        # Split the input path by "/"
        nums = pat.split("/")
        result = []

        for num in nums:
            if num == "..":  # Go back one directory
                if result:
                    result.pop()
            elif num and num != ".":  # Ignore empty parts and current directory markers
                result.append(num)

        # Join the valid parts with "/" and return the simplified path
        return "/" + "/".join(result)