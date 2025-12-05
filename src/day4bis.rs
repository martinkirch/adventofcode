pub fn mkmap(input:&String) -> Vec<Vec<u8>> {
    let mut map = Vec::new();
    for line in input.lines(){
        let mut parsed = Vec::new();
        for c in line.chars() {
            if c == '@' {
                parsed.push(1);
            } else {
                parsed.push(0);
            }
        }
        map.push(parsed);
    }
    return map;
}

const INF:usize = 999999;
const EMPTY:Vec<u8> = Vec::new();

pub fn count_adjacent_rolls(map:&Vec<Vec<u8>>, x:usize, y:usize) -> u8 {
    let mut count = 0;
    count += map.get(x.checked_sub(1).unwrap_or(INF)).unwrap_or(&EMPTY).get(y.checked_sub(1).unwrap_or(INF)).unwrap_or(&0);
    count += map.get(x.checked_sub(1).unwrap_or(INF)).unwrap_or(&EMPTY).get(y  ).unwrap_or(&0);
    count += map.get(x.checked_sub(1).unwrap_or(INF)).unwrap_or(&EMPTY).get(y.checked_add( 1).unwrap_or(INF)).unwrap_or(&0);
    count += map.get(x).unwrap_or(&EMPTY).get(y.checked_sub(1).unwrap_or(INF)).unwrap_or(&0);
    count += map.get(x).unwrap_or(&EMPTY).get(y.checked_add(1).unwrap_or(INF)).unwrap_or(&0);
    count += map.get(x.checked_add( 1).unwrap_or(INF)).unwrap_or(&EMPTY).get(y.checked_sub(1).unwrap_or(INF)).unwrap_or(&0);
    count += map.get(x.checked_add( 1).unwrap_or(INF)).unwrap_or(&EMPTY).get(y  ).unwrap_or(&0);
    count += map.get(x.checked_add( 1).unwrap_or(INF)).unwrap_or(&EMPTY).get(y.checked_add( 1).unwrap_or(INF)).unwrap_or(&0);
    return count;
}

pub fn compute(input:&String) -> String {
    let mut map = mkmap(input);
    let size = map.len();
    let mut accessible = 1;
    let mut total_fetched = 0;
    while accessible != 0 {
        accessible = 0;
        let mut next_map = map.clone();
        for x in 0..size {
            for y in 0..size {
                if map[x][y] == 1 && count_adjacent_rolls(&map, x, y) < 4 {
                    accessible += 1;
                    next_map[x][y] = 0;
                }
            }
        }
        total_fetched += accessible;
        map = next_map;
    }
    
    return total_fetched.to_string();
}

#[cfg(test)]
mod tests {
    use super::*;

    const EXAMPLE:&str = "..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
";

    #[test]
    fn test_counter() {
        let map = mkmap(&EXAMPLE.to_string());
        assert_eq!(count_adjacent_rolls(&map, 0, 2), 3);
        assert_eq!(count_adjacent_rolls(&map, 1, 9), 4);
        assert_eq!(count_adjacent_rolls(&map, 9, 9), 2);
    }

    #[test]
    fn it_works() {
        let result = compute(&EXAMPLE.to_string());
        assert_eq!(result, "43");
    }
}
