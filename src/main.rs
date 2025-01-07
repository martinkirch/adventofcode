use std::env;
use std::fs;
use crate::day1::compute as day1;
use crate::day1bis::compute as day1bis;
use crate::day2::compute as day2;
use crate::day2bis::compute as day2bis;

pub mod day1;
pub mod day1bis;
pub mod day2;
pub mod day2bis;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 1 {
        panic!("give the day number ! 1 or 1bis");
    }
    let day = args[1].as_str();
    let file = format!("input{}.txt", day);
    let input = fs::read_to_string(&file).unwrap_or_else(|_| panic!("Could not read input file: {}", file));
    match day {
        "1" => println!("{}", day1(&input)),
        "1bis" => println!("{}", day1bis(&input)),
        "2" => println!("{}", day2(&input)),
        "2bis" => println!("{}", day2bis(&input)),
        _ => panic!("Invalid day number"),
    }
}
