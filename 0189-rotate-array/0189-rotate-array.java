class Solution {
    public void rotate(int[] nums, int k) {
        int size = nums.length;
        int[] new_arr = new int[size]; // Corrected array declaration

        // Adjust k to prevent redundant rotations
        k = k % size;

        if (k != 0) { // Simplified condition
            for (int i = 0; i < size; i++) {
                new_arr[(i + k) % size] = nums[i]; // Populate the new rotated array
            }
            for (int i = 0; i < size; i++) {
                nums[i] = new_arr[i]; // Copy back to the original array
            }
        }
    }
}