pub fn deltaok(levels:&Vec<i32>, basedelta:i32, tolerate:bool, i:usize, j:usize) -> bool {
    let delta = levels[j] - levels[i];
    if delta == 0 || delta > 3 || delta < -3 || 
        (delta > 0 && basedelta < 0) || (delta < 0 && basedelta > 0) {
        if tolerate {
            let maybe = deltaok(levels, basedelta, false, i-1, j);
            if maybe {
                return true;
            }
            if j == levels.len() - 1 {
                return true;
            }
            return deltaok(levels, basedelta, false, i, j+1);
        }
        return false;
    }
    if j == levels.len() - 1 {
        return true;
    } else {
        return deltaok(levels, basedelta, tolerate, i+1, j+1);
    }

}

pub fn is_safe(levels:&Vec<i32>) -> bool {
    let delta = levels[1] - levels[0];
    let maybe = 
        if delta == 0 || delta > 3 || delta < -3 {
            false;
        } else {
            deltaok(levels, delta, true, 1, 2);
        }
    
    if !maybe {
        let delta2 = levels[2] - levels[0];
        if !(delta2 == 0 || delta2 > 3 || delta2 < -3) {
            let maybe = deltaok(levels, delta2, false, 2, 3);
            if maybe {
                return true;
            }
        }
        let delta3 = levels[2] - levels[1];
        if delta3 == 0 || delta3 > 3 || delta3 < -3 {
            return false;
        } else {
            return deltaok(levels, delta3, false, 2, 3);
        }
    }
    return false;
    
}

pub fn compute(input:&String) -> String {
    let mut nb_safe = 0;
    for report in input.lines() {
        let levels = report.split_whitespace();
        let mut levels_int = Vec::new();
        for level in levels {
            levels_int.push(level.parse::<i32>().unwrap());
        }
        if is_safe(&levels_int) {
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
        assert_eq!(true, is_safe(&vec![12, 6, 4, 2, 1]));
        assert_eq!(true, is_safe(&vec![7, 6, 4, 2, 1]));
        assert_eq!(true, is_safe(&vec![7, 12, 4, 2, 1]));
        assert_eq!(true, is_safe(&vec![7, 8, 4, 2, 1]));
        assert_eq!(false, is_safe(&vec![1, 2, 7, 8, 9]));
        assert_eq!(false, is_safe(&vec![9, 7, 6, 2, 1]));
        assert_eq!(true, is_safe(&vec![1, 3, 2, 4, 5]));
        assert_eq!(true, is_safe(&vec![8, 6, 4, 4, 1]));
        assert_eq!(true, is_safe(&vec![1, 3, 6, 7, 9]));
        assert_eq!(true, is_safe(&vec![1, 3, 6, 7, 12]));
        assert_eq!(true, is_safe(&vec![8, 6, 4, 5, 1]));
    }

    #[test]
    fn it_works() {
        let result = compute(&"7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9".to_string());
        assert_eq!(result, "4");
    }
}
