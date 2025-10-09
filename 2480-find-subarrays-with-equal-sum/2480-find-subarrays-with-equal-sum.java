class Solution {
    public boolean findSubarrays(int[] nums) {
        int n = nums.length;
        boolean answer=false;
        if(n<=2)
            return answer;
        int sum = 0;
        for(int i=0;i<n-2;i++){
            sum = nums[i]+nums[i+1];
            for(int j=i+1;j<n-1;j++){
                if(nums[j]+nums[j+1]==sum){
                    answer = true;
                }
            }
        }
        return answer;
    }
}