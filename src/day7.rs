use std::collections::BTreeSet;

pub fn compute(input:&String) -> String {
    let mut map:Vec<Vec<bool>> = input.lines().map(|line| line.bytes().map(|c| match c {
        b'^' => true,
        _ => false,
    }).collect()).collect();
    let mut splits_counter = 0;
    let starter = input.find('S').unwrap();
    let mut beams_columns = vec![starter];
    map.remove(0);
    for line in map {
        let mut next_beams_columns = BTreeSet::new();
        for col in beams_columns {
            if line[col] {
                splits_counter += 1;
                next_beams_columns.insert(col-1);
                next_beams_columns.insert(col+1);
            } else {
                next_beams_columns.insert(col);
            }
        }
        beams_columns = next_beams_columns.into_iter().collect();
    }

    return splits_counter.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = compute(&".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............".to_string());
        assert_eq!(result, "21");
    }
}
