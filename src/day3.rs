pub fn maxjoltage(input:&str) -> u32 {
    let mut i = '0';
    let mut i_max = 0;
    let mut j = '0';
    for (index, c) in input.char_indices() {
        if c > i && index < input.len() - 1 {
            i = c;
            i_max = index;
        }
    }
    for (index, c) in input.char_indices() {
        if c > j && index > i_max {
            j = c;
        }
    }
    let mut res = i.to_string();
    res.push(j);
    return res.parse::<u32>().unwrap();
}

pub fn compute(input:&String) -> String {
    return input.lines().map(|bank| maxjoltage(bank)).sum::<u32>().to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_maxjoltage() {
        assert_eq!(98, maxjoltage("987654321111111"));
        assert_eq!(89, maxjoltage("811111111111119"));
        assert_eq!(78, maxjoltage("234234234234278"));
        assert_eq!(92, maxjoltage("818181911112111"));
    }

    #[test]
    fn it_works() {
        let result = compute(&"987654321111111
811111111111119
234234234234278
818181911112111".to_string());
        assert_eq!(result, "357");
    }
}
