impl Solution {
    fn convert_char_to_int(c: char) -> i32 {
        match c {
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
            _ => todo!(),
        }
    }

    pub fn roman_to_int(s: String) -> i32 {
        let mut res = 0;
        let mut last_num = -1;
        for c in s.chars().rev() {
            let num = Self::convert_char_to_int(c);
            if last_num == num || last_num == -1 {
                res += num;
            } else {
                if num < res {
                    res -= num;
                } else {
                    res += num;
                }
            }
            last_num = num;
        }

        res
    }
}