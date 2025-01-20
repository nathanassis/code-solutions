impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x = x.to_string();
        x == x.chars().rev().collect::<String>()
    }
}