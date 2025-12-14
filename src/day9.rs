pub fn compute(input:&String) -> String {
    let positions:Vec<Vec<u64>> = input.lines().map(|line| line.split(',').map(|x| x.parse::<u64>().unwrap()).collect()).collect();

    let mut largest_area = 0;

    for (i, item) in positions.iter().enumerate() {
        for j in i+1..positions.len() {
            let other = &positions[j];
            let area = (item[0].abs_diff(other[0]) + 1) * (item[1].abs_diff(other[1]) + 1);
            if area > largest_area {
                largest_area = area;
            }
        }
    }

    return largest_area.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3".to_string());
        assert_eq!(result, "50");
    }
}
