class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        int n = nums.size();
        if(n<=2){
            return false;
        }
        int sum = 0;
        for(int i = 0;i<n-2;i++){
            sum = nums[i] + nums[i+1];
            for(int j = i + 1; j<n-1;j++){
                if(nums[j]+nums[j+1]==sum){
                    return true;
                }
            }
        }
        return false;
        
    }
};