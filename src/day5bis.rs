#[derive(Debug)]
pub struct FreshnessRange {
    min:u64,
    max:u64,
}

impl FreshnessRange {
    pub fn contains(&self, ingredient:u64) -> bool {
        self.min <= ingredient && ingredient <= self.max
    }

    pub fn overlaps(&self, other:&FreshnessRange) -> bool {
        other.contains(self.min) || other.contains(self.max) || self.contains(other.min) || self.contains(other.max)
    }
}

pub fn compute(input:&String) -> String {
    let mut freshness = Vec::new();
    let mut freshcount = 0;
    for line in input.lines() {
        if line.len() == 0 {
            break;
        } else {
            let (left, right) = line.split_once('-').unwrap();
            freshness.push(FreshnessRange {
                min: left.parse::<u64>().unwrap(),
                max: right.parse::<u64>().unwrap(),
            });
        }
    }
    let mut merged = 1;
    while merged > 0 {
        freshness.sort_by(|a, b| a.min.cmp(&b.min));
        // println!("after sort: {freshness:?}");
        let mut i = 0;
        merged = 0;
        while i < freshness.len() - 1 {
            if freshness[i].overlaps(&freshness[i+1]) {
                if freshness[i+1].max > freshness[i].max {
                    let low = &freshness[i];
                    let h = &freshness[i+1];
                    // println!("Merging: {low:?} absorbs {h:?}");
                    freshness[i].max = freshness[i+1].max;
                }
                freshness.remove(i+1);
                merged += 1;
            } else {
                i += 1;
            }
        }
    }
    for remaining in freshness {
        freshcount += remaining.max - remaining.min + 1;
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
        assert_eq!(result, "14");
    }
}
