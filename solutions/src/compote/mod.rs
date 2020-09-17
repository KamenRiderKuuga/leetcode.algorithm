use std::cmp;
// Compote
// https://codeforces.com/problemset/problem/746/A
pub fn calculate_max_total(lemons_num: f64, apples_num: f64, pears_num: f64) -> usize {
    let apple_max = (apples_num / 2 as f64).floor() as usize;
    let pears_max = (pears_num / 4 as f64).floor() as usize;
    let min_num = cmp::min(pears_max, cmp::min(lemons_num as usize, apple_max));

    min_num + 2 * min_num + 4 * min_num
}
