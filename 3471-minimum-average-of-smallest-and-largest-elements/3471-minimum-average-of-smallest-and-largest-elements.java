class Solution {
    public double minimumAverage(int[] nums) {
        double min_avg = Double.POSITIVE_INFINITY;
        Arrays.sort(nums);
        // double avg = 0;
        // int len = nums.length/2;
        for(int i = 0;i<nums.length/2;i++){
            double avg = (nums[i] + nums[nums.length-1-i]) / 2.0;
            min_avg = Math.min(min_avg, avg);
        }
        return min_avg;
    }
}