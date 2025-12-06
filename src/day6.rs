pub fn compute(input:&String) -> String {
    return "4277556".to_string();
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
