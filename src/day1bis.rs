pub fn compute(input:&String) -> String {
    /* The dial starts by pointing at 50.
     The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence. */
    let mut dial = 50;
    let mut counter = 0;
    for line in input.lines() {
        let mut delta = match line.chars().nth(0).unwrap() {
            'L' => - line[1..].parse::<i32>().unwrap(),
            'R' => line[1..].parse::<i32>().unwrap(),
            _ => panic!("incorrect first letter in {}", line)
        };

        // complete turns
        counter += delta.abs()/100;
        delta = delta % 100;

        // last one
        if (dial < 100 && dial + delta >= 100)  || 
            (dial + delta <= 0 && 0 < dial) {
            counter += 1
        }
        dial = (dial + delta + 100) % 100;

        // println!("{}: {} passes on zero, dial at {}", line, counter, dial);
    }
    return counter.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_assumptions() {
        // not sure about my Rust arithmetics
        let mut dial = -2;
        assert_eq!((-dial) / 100 + 1, 1);
        dial = -102;
        assert_eq!((-dial) / 100 + 1, 2);
        dial = 99;
        assert_eq!(dial/100, 0);
        dial = 101;
        assert_eq!(dial/100, 1);
        dial = -99;
        assert_eq!(dial/100, 0);
        dial = -101;
        assert_eq!(dial/100, -1);
        dial = -99;
        assert_eq!(dial%100, -99);
        dial = -101;
        assert_eq!(dial%100, -1);
    }

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
L82
".to_string());
        assert_eq!(result, "6");
    }

    #[test]
    fn it_works_100() {
        let result = compute(&"L50
L79
R79
".to_string());
        assert_eq!(result, "2");
    }

    #[test]
    fn it_works_harder() {
        let result = compute(&"L168
L30
R248
L5
R60
L55
L1
L99
R14
L82
".to_string());
        assert_eq!(result, "9");
    }
}
