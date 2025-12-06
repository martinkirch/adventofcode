pub fn compute(input:&String) -> String {
    let mut lines:Vec<_> = input.lines().collect();
    let operations = lines.pop().unwrap();
    
    let mut column_positions = Vec::new();
    for (i, c) in operations.chars().enumerate() {
        if c == '*' || c == '+' {
            column_positions.push(i);
        }
    }
    column_positions.push(operations.len()+1);

    let mut grand_total:u64 = 0;
    for c in 0..(column_positions.len() - 1) {
        let col_min = column_positions[c];
        let col_max = column_positions[c+1]-1; // exclusive, because at -1 it's a space

        let mut numbers = Vec::new();
        
        for i in col_min..col_max {
            let mut number = String::new();
            for line in lines.iter() {
                if line.get(i..i+1) != Some(" ") {
                    number.push_str(line.get(i..i+1).unwrap());
                }
            }
            numbers.push(number.parse::<u64>().unwrap());
        }

        grand_total += match operations.get(col_min..col_min+1) {
            Some("+") => numbers.iter().sum::<u64>(),
            Some("*") => numbers.iter().product::<u64>(),
            _ => panic!("unknown op at column {}", col_min),
        }
    }



    return grand_total.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
".to_string());
        assert_eq!(result, "3263827");
    }
}
