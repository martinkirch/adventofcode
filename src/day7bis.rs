use std::collections::HashMap;

pub fn beam(cache:&mut HashMap<(usize,usize),u64>, map:&Vec<Vec<bool>>, line:usize, col:usize) -> u64 {
    if line == map.len() {
        1
    } else if let Some(counter) = cache.get(&(line, col)) {
        *counter
    } else if map[line][col] {
        let result = beam(cache, map, line+1, col-1) + beam(cache, map, line+1, col+1);
        cache.insert((line, col), result);
        result
    } else {
        let result = beam(cache, map, line+1, col);
        cache.insert((line, col), result);
        result
    }
}


pub fn compute(input:&String) -> String {
    let map:Vec<Vec<bool>> = input.lines().map(|line| line.bytes().map(|c| match c {
        b'^' => true,
        _ => false,
    }).collect()).collect();
    let mut cache:HashMap<(usize,usize),u64> = HashMap::new();
    let starter = input.find('S').unwrap();
    return beam(&mut cache, &map, 1, starter).to_string();
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
        assert_eq!(result, "40");
    }
}
