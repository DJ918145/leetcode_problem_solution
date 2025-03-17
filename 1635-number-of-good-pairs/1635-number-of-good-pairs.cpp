class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int i, j, count = 0 ;
        int size = nums.size();
        for(i=0;i<size;i++)
        {
            for(j=0;j<size;j++)
            {
                if(nums[i] == nums[j] && i<j)
                {
                    count = count + 1;
                }
            }
        }
        return count;
    }
};