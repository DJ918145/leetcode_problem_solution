int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int i=0;
    int count = 0;
    int max = 0;
    while(i!=numsSize){
        if(nums[i]!=1){
            if(max<count){
                max = count;
            }
            count = 0;
        }
        else{
            count += 1;
        }
        i += 1;
    }
    if(max<count){
        max = count;
    }
    return max;
}