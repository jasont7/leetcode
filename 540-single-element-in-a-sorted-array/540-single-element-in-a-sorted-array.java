class Solution {
    public int singleNonDuplicate(int[] nums) {
        return findSingleElement(nums, 0, nums.length-1);
    }

    private int findSingleElement(int[] nums, int l, int r) {
        if (l == r || nums.length == 1)
            return nums[l];

        int mid = (l+r)/2;
        if (nums[mid] != nums[mid+1] && nums[mid] != nums[mid-1]) // mid-point is single
            return nums[mid];

        int l_len, r_len;
        boolean mid_left;
        if (nums[mid] == nums[mid+1]) { // mid-point duplicate is on right side
            r_len = (r-mid)+1;
            l_len = mid;
            mid_left = false;
        } else { // mid-point duplicate is on left side
            l_len = mid+1;
            r_len = r-mid;
            mid_left = true;
        }

        if (mid_left) { // mid-point duplicate is on the left side
            if (l_len % 2 == 0) // left side is even-length: search right side
                return findSingleElement(nums, mid+1, r);
            else // left side is odd-length: search left side
                return findSingleElement(nums, l, mid);
        }
        else { // mid-point duplicate is on the right side
            if (r_len % 2 == 0) // right side is even-length: search the left side
                return findSingleElement(nums, l, mid-1);
            else // right side is odd-length: search right side
                return findSingleElement(nums, mid, r);
        }
    }
}