class Solution {
    public int maxSubArray(int[] nums) {
        int currentMax = nums[0];
        int maxSum = nums[0];

        for (int i=1; i < nums.length; i++) {
            if (currentMax + nums[i] < nums[i])
                currentMax = nums[i];
            else currentMax += nums[i];

            if (currentMax > maxSum)
                maxSum = currentMax;
        }
        return maxSum;
    }
}