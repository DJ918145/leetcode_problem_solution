class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Backtracking function
        def backtrack(index, current_combination):
            if index == len(digits):
                # Add the complete combination to the result
                combinations.append("".join(current_combination))
                return
            
            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                # Add the letter to the current combination
                current_combination.append(letter)
                # Move to the next digit
                backtrack(index + 1, current_combination)
                # Backtrack to explore other possibilities
                current_combination.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations 
        