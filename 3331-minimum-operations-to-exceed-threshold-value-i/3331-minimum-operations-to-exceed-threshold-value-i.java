class Solution {
    public int minOperations(int[] nums, int k) {
        int answer = 0;
        int size = nums.length;
        for(int i=0;i<size;i++){
            if(nums[i]<k){
                answer = answer + 1;
            }
        }
        return answer;
    }
}