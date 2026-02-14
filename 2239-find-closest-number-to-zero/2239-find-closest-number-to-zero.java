class Solution {
    public int findClosestNumber(int[] nums) {
        int n = nums.length;
        int ans = nums[0];
        for(int i= 0; i<n; i++){
            if(Math.abs(nums[i])<Math.abs(ans) || (nums[i] > ans && Math.abs(nums[i])==Math.abs(ans)))
                ans = nums[i];
        }
        return ans;
    }
}