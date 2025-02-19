package leetcode;

public final class SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        int start = 0, end = nums.length - 1;
        while (start <= end) {
            int ref = (start + end) / 2;
            if (nums[ref] == target) {
                return ref;
            } else if (nums[ref] < target) {
                start = ref + 1;
            } else {
                end = ref - 1;
            }
        }

        return start;
    }
}
