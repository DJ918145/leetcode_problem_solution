class Solution(object):
    def gcdOfStrings(self, str1, str2):
        # Helper function to check if `s1` can be constructed by repeating `base`
        def isDivisible(s, base):
            if len(s) % len(base) != 0:
                return False
            return s == base * (len(s) // len(base))

        # Base case: If concatenating str1 and str2 in both orders does not match, no GCD exists
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD string based on the length of the inputs
        gcd_length = min(len(str1), len(str2))
        gcd_candidate = str1[:gcd_length]

        while gcd_candidate:
            if isDivisible(str1, gcd_candidate) and isDivisible(str2, gcd_candidate):
                return gcd_candidate
            gcd_candidate = gcd_candidate[:-1]  # Reduce the candidate length

        return ""