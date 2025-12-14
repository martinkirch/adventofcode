use std::env;
use std::fs;
use crate::day1::compute as day1;
use crate::day1bis::compute as day1bis;
use crate::day2::compute as day2;
use crate::day2bis::compute as day2bis;
use crate::day3::compute as day3;
use crate::day3bis::compute as day3bis;
use crate::day4::compute as day4;
use crate::day4bis::compute as day4bis;
use crate::day5::compute as day5;
use crate::day5bis::compute as day5bis;
use crate::day6::compute as day6;
use crate::day6bis::compute as day6bis;
use crate::day7::compute as day7;
use crate::day8::compute as day8;

pub mod day1;
pub mod day1bis;
pub mod day2;
pub mod day2bis;
pub mod day3;
pub mod day3bis;
pub mod day4;
pub mod day4bis;
pub mod day5;
pub mod day5bis;
pub mod day6;
pub mod day6bis;
pub mod day7;
pub mod day8;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        panic!("give the day number ! Like: 1 or 1bis");
    }
    let day = args[1].as_str();
    let file = format!("input{}.txt", day);
    let input = fs::read_to_string(&file).unwrap_or_else(|_| panic!("Could not read input file: {}", file));
    match day {
        "1bis" => println!("{}", day1bis(&input)),
        "1" => println!("{}", day1(&input)),
        "2" => println!("{}", day2(&input)),
        "2bis" => println!("{}", day2bis(&input)),
        "3" => println!("{}", day3(&input)),
        "3bis" => println!("{}", day3bis(&input)),
        "4" => println!("{}", day4(&input)),
        "4bis" => println!("{}", day4bis(&input)),
        "5" => println!("{}", day5(&input)),
        "5bis" => println!("{}", day5bis(&input)),
        "6" => println!("{}", day6(&input)),
        "6bis" => println!("{}", day6bis(&input)),
        "7" => println!("{}", day7(&input)),
        "8" => println!("{}", day8(&input)),
        _ => panic!("Invalid day number: {}", day),
    }
}
