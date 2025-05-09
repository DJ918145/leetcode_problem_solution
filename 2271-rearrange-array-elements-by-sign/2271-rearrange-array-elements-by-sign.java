class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] pos = new int[n];
        int[] neg = new int[n];
        int p = 0, q = 0;
        for (int num : nums) {
            if (num >= 0) pos[p++] = num;
            else neg[q++] = num;
        }
        int[] result = new int[n];
        int i = 0, pi = 0, ni = 0;
        while (pi < p && ni < q) {
            result[i++] = pos[pi++];
            result[i++] = neg[ni++];
        }
        while (pi < p) result[i++] = pos[pi++];
        while (ni < q) result[i++] = neg[ni++];
        return result;
    }
}
