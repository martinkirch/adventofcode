pub fn compute(input:&String) -> String {
    let mut numbers = Vec::new();
    let mut operations = "";
    let mut grand_total:u64 = 0;
    for line in input.lines() {
        if line.contains('+') {
            operations = line;
        } else {
            let parsed = Vec::from_iter(line.split_ascii_whitespace().map(|n| n.parse::<u64>().unwrap()));
            numbers.push(parsed);
        }
    }
    let mut i = 0;
    for c in operations.split_ascii_whitespace() {
        let column = numbers.iter().clone().map(|l| l[i]);
        grand_total += match c {
            "+" => column.sum::<u64>(),
            "*" => column.product::<u64>(),
            _ => panic!("unknown op: {}", c),
        };
        i += 1;
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
        assert_eq!(result, "4277556");
    }
}
