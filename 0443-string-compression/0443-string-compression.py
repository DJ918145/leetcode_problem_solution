class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Position to write the compressed character
        read = 0   # Position to read the character
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count the number of occurrences of the same character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count (if more than 1)
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
