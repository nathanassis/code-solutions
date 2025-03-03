impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut prefix = String::new();
        let mut index = 0;

        for letter in strs[0].chars() {
            let mut comparison = 1;
            while comparison < strs.len() {
                if Some(letter) != strs[comparison].chars().nth(index) {
                    return prefix;
                }
                comparison += 1;
            }
            prefix.push(letter);
            index += 1;
        }

        prefix
    }
}