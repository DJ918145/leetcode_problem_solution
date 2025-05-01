class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int len = nums.size();
        if(k>len){
            k = k%len;
        }
        vector<int> new_nums(len);
        if(k%len != 0 || k != 0){
            for(int i=0;i<len;i++){
                new_nums[(i+k)%len] = nums[i];
            }
            for(int i = 0; i<len;i++){
                nums[i] = new_nums[i];
            }
        }
    }
};