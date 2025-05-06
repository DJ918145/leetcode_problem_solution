void sortColors(int* nums, int numsSize) {
    int zero = 0;
    int one = 0;
    for(int i = 0; i<numsSize; i++){
        if(nums[i]== 0){
            zero++;
        }
        else if(nums[i]== 1){
            one++;
        }
    }
    for(int j = 0;j<zero;j++){
        nums[j]=0;
    }
    for(int k=zero; k<zero+one;k++){
        nums[k]=1;
    }
    for(int z=zero+one; z<numsSize; z++){
        nums[z] = 2;
    }
}