class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_length = 0
    
        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                # Justify the current line
                spaces_to_add = maxWidth - line_length
                for i in range(spaces_to_add):
                    line[i % (len(line) - 1 or 1)] += ' '  # Distribute spaces
                result.append(''.join(line))
                line, line_length = [], 0  # Reset for the next line
            line.append(word)
            line_length += len(word)
        
        # Handle the last line (left-aligned)
        result.append(' '.join(line).ljust(maxWidth))
    
        return result