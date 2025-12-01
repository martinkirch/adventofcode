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
    let mut counter = 0;
    for i in 0..left.len() {
        counter += (left[i] - right[i]).abs();
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
        assert_eq!(result, "11");
    }
}
