use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm: HashMap<i32,i32> = HashMap::new();
        hm.insert(nums[0],0);
        for i in 1..nums.len() {
            let c = nums[i];
            let req = target - c;
            if hm.contains_key(&req) {
                return vec![i as i32, *hm.get(&req).unwrap()];
            }
            hm.insert(c,i as i32);
        }
        return vec![];
    }
}
