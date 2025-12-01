pub fn is_safe(levels:Vec<i32>) -> bool {
    let delta = levels[1] - levels[0];
    if delta == 0 || delta > 3 || delta < -3 {
        return false;
    }
    for i in 2..levels.len() {
        let delta_i = levels[i] - levels[i-1];
        if delta_i == 0 || delta_i > 3 || delta_i < -3 {
            return false;
        }
        if (delta_i > 0 && delta < 0) || (delta_i < 0 && delta > 0) {
            return false;
        }
    }
    return true;
}

pub fn compute(input:&String) -> String {
    let mut nb_safe = 0;
    for report in input.lines() {
        let levels = report.split_whitespace();
        let mut levels_int = Vec::new();
        for level in levels {
            levels_int.push(level.parse::<i32>().unwrap());
        }
        if is_safe(levels_int) {
            nb_safe += 1;
        }
    }
    return nb_safe.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn safe_check() {
        assert_eq!(true, is_safe(vec![7, 6, 4, 2, 1]));
        assert_eq!(false, is_safe(vec![1, 2, 7, 8, 9]));
        assert_eq!(false, is_safe(vec![9, 7, 6, 2, 1]));
        assert_eq!(false, is_safe(vec![1, 3, 2, 4, 5]));
        assert_eq!(false, is_safe(vec![8, 6, 4, 4, 1]));
        assert_eq!(true, is_safe(vec![1, 3, 6, 7, 9]));
    }

    #[test]
    fn it_works() {
        let result = compute(&"7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9".to_string());
        assert_eq!(result, "2");
    }
}
