pub fn compute(input:&String) -> String {
    /* The dial starts by pointing at 50.
     The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence. */
    let mut dial = 50;
    let mut counter = 0;
    return counter.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"L68
L30
R48
L5
R60
L55
L1
L99
R14
L82".to_string());
        assert_eq!(result, "3");
    }
}
