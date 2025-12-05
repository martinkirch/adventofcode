struct Range {
    highest: u64,
    current_half: u64,
}

impl Range {
    fn new(l:u64, h:u64) -> Range {
        let l_repr = l.to_string();
        let current = if l_repr.len() % 2 == 0 {
            l_repr[0..l_repr.len()/2].parse::<u64>().unwrap()
        } else if l_repr.len() == 1 {
            1
        } else {
            10_u64.pow((l_repr.len() / 2).try_into().unwrap())
        };

        Range {
            highest: h,
            current_half: current,
        }
    }
}

impl Iterator for Range {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let candidate = (self.current_half.to_string() + &self.current_half.to_string()).parse::<u64>().unwrap();
        if candidate <= self.highest {
            self.current_half += 1;

            Some(candidate)
        } else {
            None
        }
    }
}

pub fn compute(input:&String) -> String {
    let mut invalid_ids_sum = 0;
    for item in input.strip_suffix("\n").unwrap().split(',') {
        let mut raw = item.split('-').map(|x| x.parse::<u64>().unwrap());
        let lower = raw.next().unwrap();
        let higher = raw.next().unwrap();

        let range = Range::new(lower, higher);
        for i in range {
            if i >= lower {
                invalid_ids_sum += i;
            }
        }
    }
    return invalid_ids_sum.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".to_string());
        assert_eq!(result, "4174379265");
    }
}
