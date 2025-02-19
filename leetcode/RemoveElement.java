package leetcode;

public final class RemoveElement {
    public static int removeElement(int[] nums, int val) {
        int i = 0, last = nums.length - 1;
        while (i <= last) {
            if (nums[i] == val) {
                nums[i] = nums[last];
                nums[last] = val;
                last--;
            } else {
                i++;
            }
        }

        return i;
    }
}
