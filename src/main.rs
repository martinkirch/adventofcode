use std::env;
use std::fs;
use crate::day1::compute as day1;

pub mod day1;

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
        _ => panic!("Invalid day number"),
    }
}
