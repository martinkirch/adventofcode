use std::collections::VecDeque;

pub fn maxjoltage(input:&str) -> u64 {
    let mut digits = VecDeque::with_capacity(12);
    let mut i_max:isize = -1;
    for rank in (0..12).rev() {
        let mut i = '0';
        let max_i = input.len() - rank;
        for (index, c) in input.char_indices() {
            let idx = index.try_into().unwrap();
            if idx > i_max && index < max_i  && c > i {
                i = c;
                i_max = idx;
            }
        }
        digits.push_back(i);
    }
    let mut res = digits.pop_front().unwrap().to_string();
    for d in digits {
        res.push(d);
    }
    return res.parse::<u64>().unwrap();
}

pub fn compute(input:&String) -> String {
    return input.lines().map(|bank| maxjoltage(bank)).sum::<u64>().to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_maxjoltage() {
        assert_eq!(811111111119, maxjoltage("811111111111119"));
        assert_eq!(987654321111, maxjoltage("987654321111111"));
        assert_eq!(434234234278, maxjoltage("234234234234278"));
        assert_eq!(888911112111, maxjoltage("818181911112111"));
    }

    #[test]
    fn it_works() {
        let result = compute(&"987654321111111
811111111111119
234234234234278
818181911112111".to_string());
        assert_eq!(result, "3121910778619");
    }
}
