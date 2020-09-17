use std::collections::HashMap;

// 两数之和
// https://leetcode-cn.com/problems/two-sum/
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut scores: HashMap<i32, i32> = HashMap::new();
    for (index, num) in nums.iter().enumerate() {
        if scores.contains_key(num) {
            return vec![*scores.get(num).unwrap(), index as i32];
        }
        scores.insert(target - num, index as i32);
    }

    return Vec::new();
}
