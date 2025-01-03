pub fn compute(input:&String) -> String {
    let mut left = Vec::new();
    let mut right = Vec::new();
    for line in input.lines() {
        let mut splitted = line.split_whitespace();
        let a = splitted.next().unwrap().parse::<i32>().unwrap();
        let b = splitted.next().unwrap().parse::<i32>().unwrap();
        left.push(a);
        right.push(b);
    }
    left.sort();
    right.sort();
    let mut left_i = 0;
    let mut right_i = 0;
    let mut counter = 0;
    while left_i < left.len() && right_i < right.len() {
        if left[left_i] < right[right_i] {
            left_i += 1;
        } else if left[left_i] > right[right_i] {
            right_i += 1;
        } else {
            let mut occurrences = 1;
            let mut j = right_i + 1;
            while let Some(next) = right.get(j) {
                if *next == left[left_i] {
                    occurrences += 1;
                    j += 1;
                } else {
                    break;
                }
            }
            counter += left[left_i] * occurrences;
            left_i += 1;
        }
    }

    return counter.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"3   4
4   3
2   5
1   3
3   9
3   3".to_string());
        assert_eq!(result, "31");
    }

    #[test]
    fn right_list_starts_smaller() {
        let result = compute(&"3   4
4   3
2   5
1   3
3   -1
3   3".to_string());
        assert_eq!(result, "31");
    }
}
