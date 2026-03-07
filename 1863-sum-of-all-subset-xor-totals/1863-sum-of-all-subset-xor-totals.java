class Solution {
    public int subsetXORSum(int[] nums) {
        int orResult = 0;
        for (int num : nums) {
            orResult |= num;
        }
        // Result is (OR of all elements) * 2^(n-1)
        return orResult << (nums.length - 1);
    }
}