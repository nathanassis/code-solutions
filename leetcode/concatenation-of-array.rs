impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let nums_clone = nums.clone();
        [nums, nums_clone].concat()
    }
}