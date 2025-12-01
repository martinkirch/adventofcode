pub fn compute(input:&String) -> String {
    return "123".to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"lol".to_string());
        assert_eq!(result, "123");
    }
}
