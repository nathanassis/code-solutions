package leetcode;

import java.util.HashMap;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int temp = target - nums[i];
            if (map.containsKey(nums[i])) {
                int[] res = { map.get(nums[i]), i };
                return res;
            }
            map.put(temp, i);
        }

        return null;
    }
}