// F - Display Size
// https://codeforces.com/problemset/problem/747/A
pub fn display_size(all_pixels: usize) -> (usize, usize) {
    let sqrt_num = (all_pixels as f64).sqrt();
    if sqrt_num == sqrt_num as usize as f64 {
        return (sqrt_num as usize, sqrt_num as usize);
    } else {
        let mut sqrt_num = sqrt_num.floor() as usize;
        loop {
            let b = all_pixels / sqrt_num;

            if sqrt_num * b == all_pixels {
                return (sqrt_num, b);
            }
            sqrt_num -= 1;
        }
    }
}