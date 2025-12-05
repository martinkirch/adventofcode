pub struct FreshnessRange {
    min:u64,
    max:u64,
}

impl FreshnessRange {
    pub fn contains(&self, ingredient:u64) -> bool {
        self.min <= ingredient && ingredient <= self.max
    }
}


pub fn compute(input:&String) -> String {
    let mut firsthalf = true;
    let mut freshness = Vec::new();
    let mut freshcount = 0;
    for line in input.lines() {
        if line.len() == 0 {
            firsthalf = false;
        } else if firsthalf {
            let (left, right) = line.split_once('-').unwrap();
            freshness.push(FreshnessRange {
                min: left.parse::<u64>().unwrap(),
                max: right.parse::<u64>().unwrap(),
            });
        } else {
            let ingredient = line.parse::<u64>().unwrap();
            for r in &freshness {
                if r.contains(ingredient) {
                    freshcount += 1;
                    break;
                }
            }
        }
    }

    return freshcount.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&"3-5
10-14
16-20
12-18

1
5
8
11
17
32".to_string());
        assert_eq!(result, "3");
    }
}
